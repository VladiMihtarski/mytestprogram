#include <iostream>
#include <vector>
using namespace std;

void simulateNestedLoops(int n, vector<int>& currentLoop) {
    if (currentLoop.size() == n) {
        for (int i = 0; i < n; i++) {
            cout << currentLoop[i] << " ";
        }
        cout << endl;
        return;
    }

    for (int i = 1; i <= n; i++) {
        currentLoop.push_back(i);
        simulateNestedLoops(n, currentLoop);
        currentLoop.pop_back();
    }
}

int main() {
    int n;
    cout << "Въведете стойността на n: ";
    cin >> n;

    vector<int> currentLoop;
    simulateNestedLoops(n, currentLoop);

    return 0;
}
