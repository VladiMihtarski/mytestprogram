#include <iostream>
#include <vector>
#include <string>

int findIndex(const std::vector<std::string>& array, const std::string& element) {
    for (int i = 0; i < array.size(); ++i) {
        if (array[i] == element) {
            return i;
        }
    }
    return -1;
}

int main() {
    std::vector<std::string> array;
    std::string element;

    std::string input;
    std::getline(std::cin, input);
    size_t pos = 0;
    std::string token;
    while ((pos = input.find(' ')) != std::string::npos) {
        token = input.substr(0, pos);
        array.push_back(token);
        input.erase(0, pos + 1);
    }
    array.push_back(input);

    std::getline(std::cin, element);

    int index = findIndex(array, element);
    std::cout << index << std::endl;

    return 0;
}
