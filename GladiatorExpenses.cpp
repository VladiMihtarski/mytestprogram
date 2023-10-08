#include <iostream>
#include <iomanip>  // Include the header for setprecision

double calculateGladiatorExpenses(int lostFights, double helmetPrice, double swordPrice, double shieldPrice, double armorPrice) {
    int totalHelmetBroken = lostFights / 2;
    int totalSwordBroken = lostFights / 3;
    int totalShieldBroken = lostFights / (2 * 3);
    int totalArmorBroken = totalShieldBroken / 2;
    double expenses = totalHelmetBroken * helmetPrice +
                      totalSwordBroken * swordPrice +
                      totalShieldBroken * shieldPrice +
                      totalArmorBroken * armorPrice;
    return expenses;
}

int main() {
    int numberOfLostFights;
    double helmetPrice, swordPrice, shieldPrice, armorPrice;

    // Read input values
    std::cin >> numberOfLostFights >> helmetPrice >> swordPrice >> shieldPrice >> armorPrice;

    // Calculate expenses using the function
    double expenses = calculateGladiatorExpenses(numberOfLostFights, helmetPrice, swordPrice, shieldPrice, armorPrice);

    // Print the total expenses with 2 decimal places
    std::cout << "Gladiator expenses: " << std::fixed << std::setprecision(2) << expenses << " aureus" << std::endl;

    return 0;
}
