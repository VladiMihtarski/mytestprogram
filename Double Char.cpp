#include <iostream>
#include <string>

using namespace std;

int main() {
    string input_string;
    while (true) {
        getline(cin, input_string);
        if (input_string == "End") {
            break;
        } else if (input_string == "SoftUni") {
            continue;
        }

        string repeated_string = "";
        for (char character : input_string) {
            repeated_string += string(2, character);
        }

        cout << repeated_string << endl;
    }

    return 0;
}
