#include <iostream>
#include <cmath>

int main() {
    double a, b, c;
    std::cout << "Enter the first coefficient: ";
    std::cin >> a;
    std::cout << "Enter the second coefficient: ";
    std::cin >> b;
    std::cout << "Enter the third coefficient: ";
    std::cin >> c;

    if (a != 0.0) {
        double d = (b * b) - (4 * a * c);

        if (d == 0.0) {
            std::cout << "The roots are real and equal." << std::endl;
            double r = -b / (2 * a);
            std::cout << "The roots are " << r << " and " << r << std::endl;
        } else if (d > 0.0) {
            std::cout << "The roots are real and distinct." << std::endl;
            double r1 = (-b + std::sqrt(d)) / (2 * a);
            double r2 = (-b - std::sqrt(d)) / (2 * a);
            std::cout << "The root1 is: " << r1 << std::endl;
            std::cout << "The root2 is: " << r2 << std::endl;
        } else {
            std::cout << "The roots are imaginary." << std::endl;
            double rp = -b / (2 * a);
            double ip = std::sqrt(-d) / (2 * a);
            std::cout << "The root1 is: " << rp << " + i" << ip << std::endl;
            std::cout << "The root2 is: " << rp << " - i" << ip << std::endl;
        }
    } else {
        std::cout << "Not a quadratic equation." << std::endl;
    }

    return 0;
}
