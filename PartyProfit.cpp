#include <iostream>

std::pair<int, int> calculateCoinsPerCompanion(int numberOfCompanions, int days) {
    int coins = 0;
    for (int currentDay = 1; currentDay <= days; ++currentDay) {
        if (currentDay % 10 == 0) {
            numberOfCompanions -= 2;
        }
        if (currentDay % 15 == 0) {
            numberOfCompanions += 5;
        }
        if (currentDay % 3 == 0) {
            coins -= numberOfCompanions * 3;
        }
        if (currentDay % 5 == 0) {
            coins += numberOfCompanions * 20;
            if (currentDay % 3 == 0) {
                coins -= numberOfCompanions * 2;
            }
        }
        coins += 50;
        coins -= numberOfCompanions * 2;
    }
    int coinsPerCompanion = coins / numberOfCompanions;
    return std::make_pair(coinsPerCompanion, numberOfCompanions);
}

int main() {
    int numberOfCompanions, days;
    std::cout << "Enter the number of companions: ";
    std::cin >> numberOfCompanions;
    std::cout << "Enter the number of days: ";
    std::cin >> days;

    std::pair<int, int> result = calculateCoinsPerCompanion(numberOfCompanions, days);
    int coinsPerCompanion = result.first;
    numberOfCompanions = result.second;

    std::cout << numberOfCompanions << " companions received " << coinsPerCompanion << " coins each." << std::endl;
    return 0;
}
