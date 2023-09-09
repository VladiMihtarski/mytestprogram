#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, w;
};

class Graph {
public:
    Graph(int vertices);
    void addEdge(int u, int v, int w);
    bool bellmanFord(int src, int dest);

private:
    int V;
    vector<Edge> edges;
};

Graph::Graph(int vertices) {
    V = vertices;
}

void Graph::addEdge(int u, int v, int w) {
    edges.push_back({u, v, w});
}

bool Graph::bellmanFord(int src, int dest) {
    vector<int> dist(V, numeric_limits<int>::max());
    dist[src - 1] = 0;

    for (int i = 0; i < V - 1; i++) {
        for (const Edge &edge : edges) {
            int u = edge.u;
            int v = edge.v;
            int weight = edge.w;
            if (dist[u - 1] != numeric_limits<int>::max() && dist[u - 1] + weight < dist[v - 1]) {
                dist[v - 1] = dist[u - 1] + weight;
            }
        }
    }

    for (const Edge &edge : edges) {
        int u = edge.u;
        int v = edge.v;
        int weight = edge.w;
        if (dist[u - 1] != numeric_limits<int>::max() && dist[u - 1] + weight < dist[v - 1]) {
            return true; // Negative cycle detected
        }
    }

    if (dist[dest - 1] == numeric_limits<int>::max()) {
        cout << "No path from source to destination" << endl;
    } else {
        vector<int> path;
        int current = dest - 1;
        while (current != src - 1) {
            for (const Edge &edge : edges) {
                int u = edge.u;
                int v = edge.v;
                int weight = edge.w;
                if (dist[u - 1] + weight == dist[current]) {
                    path.push_back(current + 1);
                    current = u - 1;
                    break;
                }
            }
        }
        path.push_back(src);
        reverse(path.begin(), path.end());

        for (int node : path) {
            cout << node << " ";
        }
        cout << endl << dist[dest - 1] << endl;
    }

    return false; // No negative cycle detected
}

int main() {
    int n, e;
    cin >> n >> e;
    Graph g(n);

    for (int i = 0; i < e; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        g.addEdge(u, v, w);
    }

    int src, dest;
    cin >> src >> dest;

    if (g.bellmanFord(src, dest)) {
        cout << "Negative Cycle Detected" << endl;
    }

    return 0;
}
