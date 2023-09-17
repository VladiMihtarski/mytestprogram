#include <iostream>
#include <string>

int main() {
    std::string word;

    // Input the word
    std::cout << "Enter a word: ";
    std::cin >> word;

    // Reverse the word using a loop
    std::string reversed_word;
    for (int i = word.length() - 1; i >= 0; i--) {
        reversed_word += word[i];
    }

    // Print the reversed word
    std::cout << "Reversed word: " << reversed_word << std::endl;

    return 0;
}

