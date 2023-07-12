#include <iostream>

int getFibonacci(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return getFibonacci(n - 1) + getFibonacci(n - 2);
    }
}

int main() {
    // Четене на входното число
    int n;
    std::cin >> n;

    // Изчисляване на (n+1)-вото число на Фибоначи
    int fibonacci_number = getFibonacci(n + 1);

    // Извеждане на резултата
    std::cout << fibonacci_number << std::endl;

    return 0;
}
