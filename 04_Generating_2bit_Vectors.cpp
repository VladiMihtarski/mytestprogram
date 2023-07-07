#include <iostream>
#include <string>

void generate_bit_vectors(int n, std::string vector) {
    if (n == 0) {
        std::cout << vector << std::endl;
    } else {
        generate_bit_vectors(n - 1, vector + "0");
        generate_bit_vectors(n - 1, vector + "1");
    }
}

int main() {
    int n;
    std::cout << "Въведете брой битове (n): ";
    std::cin >> n;
    generate_bit_vectors(n, "");
    return 0;
}
