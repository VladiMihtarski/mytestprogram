#include <iostream>
#include <vector>
#include <unordered_map>
#include <sstream>

using namespace std;

void dfs(const unordered_map<int, vector<int>>& graph, int node, vector<bool>& visited, vector<int>& component) {
    visited[node] = true;
    for (int neighbor : graph.at(node)) {
        if (!visited[neighbor]) {
            dfs(graph, neighbor, visited, component);
        }
    }
    component.push_back(node);
}

vector<vector<int>> find_connected_components(const unordered_map<int, vector<int>>& graph) {
    int n = graph.size();
    vector<bool> visited(n, false);
    vector<vector<int>> connected_components;

    for (int node = 0; node < n; ++node) {
        if (!visited[node]) {
            vector<int> component;
            dfs(graph, node, visited, component);
            connected_components.push_back(vector<int>(component.rbegin(), component.rend()));
        }
    }

    return connected_components;
}

unordered_map<int, vector<int>> read_graph() {
    int n;
    cin >> n;
    cin.ignore();

    unordered_map<int, vector<int>> graph;
    for (int node = 0; node < n; ++node) {
        string line;
        getline(cin, line);
        istringstream iss(line);

        int neighbor;
        vector<int> neighbors;
        while (iss >> neighbor) {
            neighbors.push_back(neighbor);
        }

        graph[node] = neighbors;
    }

    return graph;
}

void print_connected_components(const vector<vector<int>>& connected_components) {
    for (int i = 0; i < connected_components.size(); ++i) {
        const vector<int>& component = connected_components[i];
        cout << "Connected component: ";
        for (int j = component.size() - 1; j >= 0; --j) {
            cout << component[j] << " ";
        }
        cout << endl;
    }
}

int main() {
    unordered_map<int, vector<int>> graph = read_graph();
    vector<vector<int>> connected_components = find_connected_components(graph);
    print_connected_components(connected_components);

    return 0;
}
