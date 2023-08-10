from collections import defaultdict, deque

def shortest_path(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# Read input
num_nodes = int(input())
num_edges = int(input())

graph = defaultdict(list)

for _ in range(num_edges):
    source, destination = map(int, input().split())
    graph[source].append(destination)
    graph[destination].append(source)

start_node = int(input())
end_node = int(input())

# Find shortest path
path = shortest_path(graph, start_node, end_node)

# Print output
if path:
    print("Shortest path length is:", len(path) - 1)
    print(" ".join(map(str, path)))
else:
    print("No path found between", start_node, "and", end_node)
