#include <iostream>
#include <cmath>
#include <iomanip>

int main() {
    double number;
    
    // Read a floating-point number from the user
    std::cout << "";
    std::cin >> number;

    if (number == 0) {
        std::cout << "zero" << std::endl;
    } else {
        // Initialize the label for positivity/negativity
        std::string sign_label = (number >= 0) ? "positive" : "negative";

        // Initialize the label for size
        std::string size_label = (std::abs(number) < 1) ? "small" : (std::abs(number) > 1000000) ? "large" : "";

        // Print the labels only
        if (!size_label.empty()) {
            std::cout << size_label << " " << sign_label << std::endl;
        } else {
            std::cout << sign_label << std::endl;
        }
    }

    return 0;
}
