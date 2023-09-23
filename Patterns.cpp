#include <iostream>

int main() {
    int number;
    
    // Input the number
    std::cout << "Enter a number: ";
    std::cin >> number;
    
    // Print asterisks in an increasing pattern
    for (int i = 1; i <= number; i++) {
        for (int j = 0; j < i; j++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }
    
    // Print asterisks in a decreasing pattern
    for (int i = number - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }
    
    return 0;
}
