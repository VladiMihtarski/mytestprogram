#include <iostream>
#include <vector>
#include <unordered_map>

const int GRID_SIZE = 3;
const int NUM_POINTS = GRID_SIZE * GRID_SIZE;

int getIndex(char point) {
    return point - 'A';
}

bool isValidMove(int from, int to, const std::vector<bool>& visited, const std::vector<std::vector<int>>& skip) {
    if (visited[to]) {
        return false;
    }
    if (skip[from][to] != -1 && !visited[skip[from][to]]) {
        return false;
    }
    return true;
}

int dfs(int current, int remainingLength, std::vector<bool>& visited, const std::vector<std::vector<int>>& skip) {
    if (remainingLength == 0) {
        return 1;
    }

    visited[current] = true;
    int count = 0;

    for (int i = 0; i < NUM_POINTS; ++i) {
        if (isValidMove(current, i, visited, skip)) {
            count += dfs(i, remainingLength - 1, visited, skip);
        }
    }

    visited[current] = false;
    return count;
}

unsigned int countPatternsFrom(char firstDot, unsigned short length) {
    if (length <= 0 || length > NUM_POINTS) {
        return 0;
    }

    std::vector<std::vector<int>> skip(NUM_POINTS, std::vector<int>(NUM_POINTS, -1));

    skip[getIndex('A')][getIndex('C')] = skip[getIndex('C')][getIndex('A')] = getIndex('B');
    skip[getIndex('A')][getIndex('I')] = skip[getIndex('I')][getIndex('A')] = getIndex('E');
    skip[getIndex('A')][getIndex('G')] = skip[getIndex('G')][getIndex('A')] = getIndex('D');
    skip[getIndex('B')][getIndex('H')] = skip[getIndex('H')][getIndex('B')] = getIndex('E');
    skip[getIndex('C')][getIndex('I')] = skip[getIndex('I')][getIndex('C')] = getIndex('F');
    skip[getIndex('C')][getIndex('G')] = skip[getIndex('G')][getIndex('C')] = getIndex('E');
    skip[getIndex('D')][getIndex('F')] = skip[getIndex('F')][getIndex('D')] = getIndex('E');
    skip[getIndex('G')][getIndex('I')] = skip[getIndex('I')][getIndex('G')] = getIndex('H');

    std::vector<bool> visited(NUM_POINTS, false);
    return dfs(getIndex(firstDot), length - 1, visited, skip);
}

int main() {
    std::cout << countPatternsFrom('D', 3) << std::endl; // Expected output: 37
    return 0;
}
