#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<bool>> visited;
vector<pair<pair<int, int>, int>> areas;
int rows, cols;
vector<string> matrix;

int explore_area(int row, int col) {
    if (row < 0 || row >= rows || col < 0 || col >= cols) {
        return 0;
    }
    if (matrix[row][col] != '-' || visited[row][col]) {
        return 0;
    }

    visited[row][col] = true;
    int size = 1;
    size += explore_area(row - 1, col);  // explore up
    size += explore_area(row + 1, col);  // explore down
    size += explore_area(row, col - 1);  // explore left
    size += explore_area(row, col + 1);  // explore right
    return size;
}

bool compareAreas(pair<pair<int, int>, int> a, pair<pair<int, int>, int> b) {
    if (a.second != b.second) {
        return a.second > b.second;
    }
    if (a.first.first != b.first.first) {
        return a.first.first < b.first.first;
    }
    return a.first.second < b.first.second;
}

int main() {
    cin >> rows >> cols;
    matrix.resize(rows);
    visited.resize(rows, vector<bool>(cols, false));

    for (int i = 0; i < rows; i++) {
        cin >> matrix[i];
    }

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (matrix[row][col] == '-' && !visited[row][col]) {
                int area_size = explore_area(row, col);
                areas.push_back({{row, col}, area_size});
            }
        }
    }

    sort(areas.begin(), areas.end(), compareAreas);

    cout << "Total areas found: " << areas.size() << "\n";
    for (int i = 0; i < areas.size(); i++) {
        cout << "Area #" << i + 1 << " at (" << areas[i].first.first << ", " << areas[i].first.second << "), size: " << areas[i].second << "\n";
    }

    return 0;
}
