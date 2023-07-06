#include <iostream>
#include <string>

void draw_figure(int n) {
    if (n == 0) {
        return;
    } else {
        std::cout << std::string(n, '*') << std::endl;
        draw_figure(n - 1);
        std::cout << std::string(n, '#') << std::endl;
    }
}

int main() {
    int num;
    std::cout << "Въведете число: ";
    std::cin >> num;
    draw_figure(num);
    return 0;
}
