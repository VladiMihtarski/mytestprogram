#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>
#include <iomanip>

std::vector<std::string> SplitString(const std::string& input, char delimiter) {
    std::vector<std::string> tokens;
    std::istringstream stream(input);
    std::string token;
    while (std::getline(stream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

std::tuple<std::vector<double>, double, std::string> ShopForItems(const std::string& items, double budget) {
    std::unordered_map<std::string, double> max_prices = {
        {"Clothes", 50.00},
        {"Shoes", 35.00},
        {"Accessories", 20.50}
    };

    std::vector<double> bought_items;
    double total_profit = 0.0;

    std::vector<std::string> item_list = SplitString(items, '|');

    for (const std::string& item : item_list) {
        size_t arrow_position = item.find("->");
        if (arrow_position != std::string::npos) {
            std::string item_type = item.substr(0, arrow_position);
            double item_price = std::stod(item.substr(arrow_position + 2));

            if (max_prices.find(item_type) != max_prices.end() &&
                item_price <= max_prices[item_type] && budget >= item_price) {
                budget -= item_price;
                double profit = item_price * 0.40;
                total_profit += profit;
                bought_items.push_back(item_price + profit);
            }
        }
    }

    double new_total_price = total_profit + budget;
    std::string message = (new_total_price >= 150) ? "Hello, France!" : "Not enough money";

    return std::make_tuple(bought_items, total_profit, message);
}

int main() {
    std::string input_str;
    double budget;

    std::cout << "Enter the items in the format 'Type->Price|Type->Price|...': ";
    std::getline(std::cin, input_str);

    std::cout << "Enter your budget: ";
    std::cin >> budget;

    std::vector<double> bought_items;
    double total_profit;
    std::string message;

    std::tie(bought_items, total_profit, message) = ShopForItems(input_str, budget);

    std::cout << "Items: ";
    for (double price : bought_items) {
        std::cout << std::fixed << std::setprecision(2) << price << " ";
    }
    std::cout << std::endl;

    std::cout << "Profit: " << std::fixed << std::setprecision(2) << total_profit << std::endl;

    if (message == "Hello, France!") {
        std::cout << message << std::endl;
    }

    return 0;
}
