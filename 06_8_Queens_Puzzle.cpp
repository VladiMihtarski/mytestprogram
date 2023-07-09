#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

const int BOARD_SIZE = 8;

void print_board(const vector<string>& board) {
    for (const string& row : board) {
        for (char ch : row) {
            cout << ch << " ";
        }
        cout << endl;
    }
    cout << endl;
}


bool can_put_queen(int row, int col, const unordered_set<int>& rows,
                   const unordered_set<int>& cols, const unordered_set<int>& left_diagonals,
                   const unordered_set<int>& right_diagonals) {
    if (rows.count(row) > 0) {
        return false;
    }
    if (cols.count(col) > 0) {
        return false;
    }
    if (left_diagonals.count(row - col) > 0) {
        return false;
    }
    if (right_diagonals.count(row + col) > 0) {
        return false;
    }
    return true;
}

void set_queen(int row, int col, vector<string>& board, unordered_set<int>& rows,
               unordered_set<int>& cols, unordered_set<int>& left_diagonals,
               unordered_set<int>& right_diagonals) {
    board[row][col] = '*';
    rows.insert(row);
    cols.insert(col);
    left_diagonals.insert(row - col);
    right_diagonals.insert(row + col);
}

void remove_queen(int row, int col, vector<string>& board, unordered_set<int>& rows,
                  unordered_set<int>& cols, unordered_set<int>& left_diagonals,
                  unordered_set<int>& right_diagonals) {
    board[row][col] = '-';
    rows.erase(row);
    cols.erase(col);
    left_diagonals.erase(row - col);
    right_diagonals.erase(row + col);
}

void put_queens(int row, vector<string>& board, unordered_set<int>& rows,
                unordered_set<int>& cols, unordered_set<int>& left_diagonals,
                unordered_set<int>& right_diagonals) {
    if (row == BOARD_SIZE) {
        print_board(board);
        return;
    }
    for (int col = 0; col < BOARD_SIZE; col++) {
        if (can_put_queen(row, col, rows, cols, left_diagonals, right_diagonals)) {
            set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals);
            put_queens(row + 1, board, rows, cols, left_diagonals, right_diagonals);
            remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals);
        }
    }
}

int main() {
    vector<string> board(BOARD_SIZE, string(BOARD_SIZE, '-'));
    unordered_set<int> rows, cols, left_diagonals, right_diagonals;
    put_queens(0, board, rows, cols, left_diagonals, right_diagonals);
    return 0;
}
