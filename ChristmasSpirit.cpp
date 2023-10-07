#include <iostream>

std::pair<int, int> calculateCostAndSpirit(int quantity_of_decorations, int remaining_days) {
    int total_cost = 0;
    int total_spirit = 0;

    for (int current_day = 1; current_day <= remaining_days; ++current_day) {

        // Check if it's a day to add 2 decorations.
        if (current_day % 11 == 0) {
            quantity_of_decorations += 2;
        }

        // Calculate the cost for ornaments on even days.
        if (current_day % 2 == 0) {
            total_cost += quantity_of_decorations * 2;
            total_spirit += 5;
        }

        // Calculate the cost for tree skirt and garland on days divisible by 3.
        if (current_day % 3 == 0) {
            total_cost += quantity_of_decorations * (5 + 3);
            total_spirit += 10 + 3;
        }

        // Calculate the cost for tree lights on days divisible by 5.
        if (current_day % 5 == 0) {
            total_cost += quantity_of_decorations * 15;
            total_spirit += 17;

            // Additional cost if also divisible by 3.
            if (current_day % 3 == 0) {
                total_spirit += 30;
            }
        }

        // Calculate the cost for special items on days divisible by 10.
        if (current_day % 10 == 0) {
            total_spirit -= 20;
            total_cost += 5 + 3 + 15;
        }
    }

    // If the last day is a tenth day, the cat ruins additional items.
    if (remaining_days % 10 == 0) {
        total_spirit -= 30;
    }

    return {total_cost, total_spirit};
}

int main() {
    int quantity_of_decorations, remaining_days;
    std::cin >> quantity_of_decorations >> remaining_days;

    std::pair<int, int> result = calculateCostAndSpirit(quantity_of_decorations, remaining_days);

    std::cout << "Total cost: " << result.first << std::endl;
    std::cout << "Total spirit: " << result.second << std::endl;

    return 0;
}
