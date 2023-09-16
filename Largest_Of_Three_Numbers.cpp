#include <iostream>

int main() {
    int num1, num2, num3;

    // Read three whole numbers from the user
    std::cout << "Enter the first number: ";
    std::cin >> num1;

    std::cout << "Enter the second number: ";
    std::cin >> num2;

    std::cout << "Enter the third number: ";
    std::cin >> num3;

    // Find the largest number among the three
    int largest = std::max(std::max(num1, num2), num3);

    // Print the largest number
    std::cout << "The largest number is: " << largest << std::endl;

    return 0;
}
