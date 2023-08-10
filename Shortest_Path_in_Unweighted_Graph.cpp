#include <iostream>
#include <queue>
#include <vector>
#include <map>
#include <string>
#include <sstream>

int main() {
    int nodes, edges;
    std::cin >> nodes >> edges;

    std::map<int, std::vector<int>> graph;
    for (int i = 0; i < edges; ++i) {
        int source, destination;
        std::cin >> source >> destination;
        graph[source].push_back(destination);
        graph[destination].push_back(source);
    }

    int start, end;
    std::cin >> start >> end;

    std::vector<int> dist(nodes + 1, -1);
    std::vector<int> parent(nodes + 1, -1);

    std::queue<int> q;
    q.push(start);
    dist[start] = 0;

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        for (int neighbor : graph[current]) {
            if (dist[neighbor] == -1) {
                q.push(neighbor);
                dist[neighbor] = dist[current] + 1;
                parent[neighbor] = current;
            }
        }
    }

    if (dist[end] == -1) {
        std::cout << "No path found" << std::endl;
    } else {
        std::cout << "Shortest path length is: " << dist[end] << std::endl;
        std::cout << end;

        int current = end;
        while (parent[current] != -1) {
            std::cout << " " << parent[current];
            current = parent[current];
        }
        std::cout << std::endl;
    }

    return 0;
}
