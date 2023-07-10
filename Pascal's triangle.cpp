#include <iostream>
#include <vector>
#include <string>

std::vector<std::vector<int>> generate_pascal_triangle(int height) {
    std::vector<std::vector<int>> triangle;
    for (int i = 0; i < height; i++) {
        std::vector<int> row(i + 1, 1);
        triangle.push_back(row);
    }

    for (int i = 2; i < height; i++) {
        std::vector<int>& row = triangle[i];
        for (int j = 1; j < i; j++) {
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
    }

    return triangle;
}

void print_pascal_triangle(const std::vector<std::vector<int>>& triangle) {
    int max_number_width = std::to_string(triangle.back()[triangle.back().size() / 2]).length();
    int height = triangle.size();
    for (int i = 0; i < height; i++) {
        const std::vector<int>& row = triangle[i];
        std::string spaces(height - i - 1, ' ');
        std::string numbers;
        for (int number : row) {
            numbers += std::to_string(number) + " ";
        }
        std::cout << spaces + numbers << std::endl;
    }
}

int main() {
    int height;
    std::cout << "Въведете височина на Триъгълника на Паскал: ";
    std::cin >> height;

    std::vector<std::vector<int>> triangle = generate_pascal_triangle(height);
    print_pascal_triangle(triangle);

    return 0;
}
