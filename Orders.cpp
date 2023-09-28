#include <iostream>
#include <iomanip> // Add this line for setprecision

int main() {
    int N;
    double total_price = 0.0;

    std::cout << "Enter the number of orders: ";
    std::cin >> N;

    for (int i = 0; i < N; ++i) {
        double price_per_capsule;
        int days, capsules_per_day;

        std::cout << "Enter the price per capsule: ";
        std::cin >> price_per_capsule;

        std::cout << "Enter the number of days: ";
        std::cin >> days;

        std::cout << "Enter the number of capsules needed per day: ";
        std::cin >> capsules_per_day;

        if (0.01 <= price_per_capsule && price_per_capsule <= 100.00 && 
            1 <= days && days <= 31 && 
            1 <= capsules_per_day && capsules_per_day <= 2000) {
            double order_price = price_per_capsule * days * capsules_per_day;
            
            // Add the calculated order_price to total_price
            total_price += order_price;
            
            // Use setprecision with std::fixed
            std::cout << "The price for the coffee is: $" << std::fixed << std::setprecision(2) << order_price << std::endl;
        }
    }

    // Use setprecision with std::fixed
    std::cout << "Total: $" << std::fixed << std::setprecision(2) << total_price << std::endl;

    return 0;
}
