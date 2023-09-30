#include <iostream>
#include <string>

using namespace std;

int main() {
    int coffee_count = 0;
    string event;

    while (true) {
        getline(cin, event);
        
        if (event == "END") {
            break;
        }

        if (event == "coding" || event == "dog" || event == "cat" || event == "movie") {
            coffee_count += 1;
        } else if (isupper(event[0])) {
            coffee_count += 2;
        }
    }

    if (coffee_count <= 5) {
        cout << coffee_count << endl;
    } else {
        cout << "You need extra sleep" << endl;
    }

    return 0;
}
