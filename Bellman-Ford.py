class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src, dest):
        dist = [float("inf")] * self.V
        dist[src - 1] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u - 1] != float("inf") and dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w

        # Check for negative cycles
        for u, v, w in self.graph:
            if dist[u - 1] != float("inf") and dist[u - 1] + w < dist[v - 1]:
                print("Negative Cycle Detected")
                return

        # Reconstruct the path if it exists
        path = [dest]
        current = dest - 1
        while current != src - 1:
            for u, v, w in self.graph:
                if dist[u - 1] + w == dist[current]:
                    path.append(u)
                    current = u - 1
                    break

        path.reverse()

        if dist[dest - 1] == float("inf"):
            print("No path from source to destination")
        else:
            print(" ".join(map(str, path)))
            print(dist[dest - 1])

if __name__ == "__main__":
    n = int(input())
    e = int(input())
    g = Graph(n)

    for _ in range(e):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    src = int(input())
    dest = int(input())

    g.bellman_ford(src, dest)
