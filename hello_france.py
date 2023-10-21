def shop_for_items(items, budget):
    max_prices = {
        "Clothes": 50.00,
        "Shoes": 35.00,
        "Accessories": 20.50
    }

    bought_items = []
    total_profit = 0

    for item in items:
        item_type, item_price = item.split("->")
        item_price = float(item_price)

        if item_type in max_prices and item_price <= max_prices[item_type] and budget >= item_price:
            budget -= item_price
            profit = item_price * 0.40
            total_profit += profit
            bought_items.append(item_price + profit)

    new_total_price = sum(bought_items) + budget

    if new_total_price >= 150:
        message = "Hello, France!"
    else:
        message = "Not enough money."

    return bought_items, total_profit, message

input_str = input("Enter the items in the format 'Type->Price|Type->Price|...': ")
budget = float(input("Enter your budget: "))
items = input_str.split('|')

bought_items, total_profit, message = shop_for_items(items, budget)

print(" ".join(f"{price:.2f}" for price in bought_items))
print(f"Profit: {total_profit:.2f}")
print(message)
