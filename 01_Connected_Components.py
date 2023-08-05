def dfs(graph, node, visited, component):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)
    component.append(node)

def find_connected_components(graph):
    n = len(graph)
    visited = [False] * n
    connected_components = []

    for node in range(n):
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            connected_components.append(component[::-1])

    return connected_components

def read_graph():
    n = int(input())
    graph = {}
    for node in range(n):
        neighbors = input().split()
        graph[node] = [int(neighbor) for neighbor in neighbors]
    return graph

def print_connected_components(connected_components):
    for i, component in enumerate(connected_components, 1):
        # Iterate through the component list in reverse order
        print(f"Connected component: {' '.join(str(node) for node in component[::-1])}")

def main():
    graph = read_graph()
    connected_components = find_connected_components(graph)
    print_connected_components(connected_components)

if __name__ == "__main__":
    main()
