#include <string>

int get_age(const std::string& she_said) {
    // Връщаме първия символ като число
    return she_said[0] - '0';
}