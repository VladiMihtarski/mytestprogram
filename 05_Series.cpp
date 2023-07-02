#include <iostream>
#include <iomanip>
#include <string>
#include <map>

int main() {
    std::map<std::string, double> discounts;
    discounts["Thrones"] = 0.5;
    discounts["Lucifer"] = 0.4;
    discounts["Protector"] = 0.3;
    discounts["TotalDrama"] = 0.2;
    discounts["Area"] = 0.1;

    double budget;
    int num_series;
    double total_cost = 0.0;

    std::cout << "";
    std::cin >> budget;
    std::cout << "";
    std::cin >> num_series;

    for (int i = 0; i < num_series; i++) {
        std::string series_name;
        double series_price;

        std::cout << "";
        std::cin.ignore();
        std::getline(std::cin, series_name);
        std::cout << "";
        std::cin >> series_price;

        if (discounts.find(series_name) != discounts.end()) {
            series_price -= series_price * discounts[series_name];
        }

        total_cost += series_price;
    }

    if (budget >= total_cost) {
        double remaining_money = budget - total_cost;
        std::cout << "You bought all the series and left with " << std::fixed << std::setprecision(2) << remaining_money << " lv." << std::endl;
    } else {
        double needed_money = total_cost - budget;
        std::cout << "You need " << std::fixed << std::setprecision(2) << needed_money << " lv. more to buy the series!" << std::endl;
    }

    return 0;
}
