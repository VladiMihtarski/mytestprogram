#include <iostream>
#include <sstream>
#include <vector>

int recursive_sum(const std::vector<int>& arr, int index) {
    if (index == arr.size()) {
        return 0;
    } else {
        return arr[index] + recursive_sum(arr, index + 1);
    }
}

int main() {
    std::string input;
    std::cout << "Въведете елементите на масива, разделени с интервали: ";
    std::getline(std::cin, input);

    std::istringstream iss(input);
    int num;
    std::vector<int> array;
    while (iss >> num) {
        array.push_back(num);
    }

    int total_sum = recursive_sum(array, 0);
    std::cout << "Сумата на елементите в масива е: " << total_sum << std::endl;

    return 0;
}
