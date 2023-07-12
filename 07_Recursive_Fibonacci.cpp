#include <iostream>

int getFibonacci(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    }

    int prev1 = 0;
    int prev2 = 1;
    int current;

    for (int i = 2; i <= n; i++) {
        current = prev1 + prev2;
        prev1 = prev2;
        prev2 = current;
    }

    return current;
}

int main() {
    // Четене на входното число
    int n;
    std::cin >> n;

    // Изчисляване на n-тото число на Фибоначи
    int fibonacci_number = getFibonacci(n + 1);

    // Извеждане на резултата
    std::cout << fibonacci_number << std::endl;

    return 0;
}
