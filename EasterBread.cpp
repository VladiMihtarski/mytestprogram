#include <iostream>
#include <tuple>

std::tuple<int, int, float> calculateEasterBreadLoaves(float budget, float flourPrice) {
    // Calculate the price for 1 pack of eggs and 1 liter of milk.
    float eggPrice = flourPrice * 0.75;
    float milkPrice = flourPrice * 1.25;

    // Calculate the total cost of one loaf of Easter bread.
    float loafCost = eggPrice + flourPrice + (milkPrice * 0.25);

    // Initialize variables to track the number of loaves made, the number of colored eggs collected, and the remaining budget.
    int loavesMade = 0;
    int coloredEggs = 0;
    float remainingBudget = budget;

    // While the remaining budget is greater than or equal to the cost of one loaf of bread, keep making loaves.
    while (remainingBudget >= loafCost) {
        // Make a loaf of bread.
        loavesMade++;

        // Collect 3 colored eggs for making the loaf of bread.
        coloredEggs += 3;

        // Subtract the cost of the loaf from the remaining budget.
        remainingBudget -= loafCost;

        // Every 3rd loaf, you lose some of your colored eggs.
        if (loavesMade % 3 == 0) {
            coloredEggs -= (loavesMade - 2);
        }
    }

    return std::make_tuple(loavesMade, coloredEggs, remainingBudget);
}

int main() {
    float budget, flourPrice;
    std::cin >> budget >> flourPrice;

    auto result = calculateEasterBreadLoaves(budget, flourPrice);

    int loavesMade = std::get<0>(result);
    int coloredEggs = std::get<1>(result);
    float remainingBudget = std::get<2>(result);

    std::cout << "You made " << loavesMade << " loaves of Easter bread! Now you have " << coloredEggs << " eggs and " << remainingBudget << "BGN left." << std::endl;

    return 0;
}
