#include <iostream>
#include <vector>

void dfs(std::vector<std::vector<char>>& labyrinth, std::vector<std::vector<bool>>& visited, int x, int y, std::string& path) {
    int rows = labyrinth.size();
    int cols = labyrinth[0].size();

    if (labyrinth[x][y] == 'e') {
        std::cout << path << std::endl;
        return;
    }

    visited[x][y] = true;

    std::vector<std::pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    std::vector<char> direction_symbols = {'R', 'D', 'L', 'U'};

    for (int i = 0; i < directions.size(); i++) {
        int new_x = x + directions[i].first;
        int new_y = y + directions[i].second;

        if (new_x >= 0 && new_x < rows && new_y >= 0 && new_y < cols && !visited[new_x][new_y] && labyrinth[new_x][new_y] != '*') {
            path.push_back(direction_symbols[i]);
            dfs(labyrinth, visited, new_x, new_y, path);
            path.pop_back();
        }
    }

    visited[x][y] = false;
}

void find_all_paths(std::vector<std::vector<char>>& labyrinth) {
    int rows = labyrinth.size();
    int cols = labyrinth[0].size();
    std::vector<std::vector<bool>> visited(rows, std::vector<bool>(cols, false));
    std::string path;

    dfs(labyrinth, visited, 0, 0, path);
}

int main() {
    int rows, cols;

    std::cout << "Enter the number of rows: ";
    std::cin >> rows;
    std::cout << "Enter the number of columns: ";
    std::cin >> cols;

    std::cout << "Enter the labyrinth:" << std::endl;
    std::vector<std::vector<char>> labyrinth(rows, std::vector<char>(cols));

    for (int i = 0; i < rows; i++) {
        std::string row;
        std::cin >> row;
        for (int j = 0; j < cols; j++) {
            labyrinth[i][j] = row[j];
        }
    }

    std::cout << "Paths to the exit:" << std::endl;
    find_all_paths(labyrinth);

    return 0;
}
