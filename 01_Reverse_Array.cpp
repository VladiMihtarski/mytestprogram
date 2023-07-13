#include <iostream>
#include <vector>
using namespace std;

void reverseArray(vector<int>& arr, int start, int end) {
    if (start >= end) {
        return;
    }
    
    swap(arr[start], arr[end]);
    reverseArray(arr, start + 1, end - 1);
}

string printArray(const vector<int>& arr, int start, int end) {
    if (start > end) {
        return "";
    }
    
    string result = to_string(arr[start]) + " ";
    result += printArray(arr, start + 1, end);
    
    return result;
}

int main() {
    vector<int> array;
    int size;

    cout << "Въведете размер на масива: ";
    cin >> size;

    cout << "Въведете елементите на масива: ";
    for (int i = 0; i < size; i++) {
        int element;
        cin >> element;
        array.push_back(element);
    }

    cout << "Оригинален масив:" << endl;
    cout << printArray(array, 0, size - 1) << endl;

    reverseArray(array, 0, size - 1);

    cout << "Обърнат масив:" << endl;
    cout << printArray(array, 0, size - 1) << endl;

    return 0;
}
