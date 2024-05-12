def calculate_price(day, item, quantity):
    workday_prices = {'banana': 2.50, 'apple': 1.20, 'orange': 0.85, 'grapefruit': 1.45, 'kiwi': 2.70, 'pineapple': 5.50, 'grapes': 3.85}
    weekend_prices = {'banana': 2.70, 'apple': 1.25, 'orange': 0.90, 'grapefruit': 1.60, 'kiwi': 3.00, 'pineapple': 5.60, 'grapes': 4.20}

    valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if day not in valid_days or item.lower() not in workday_prices:
        return "error"

    if day in ['Saturday', 'Sunday']:
        return "{:.2f}".format(weekend_prices[item.lower()] * quantity)
    else:
        return "{:.2f}".format(workday_prices[item.lower()] * quantity)

# Пример за използване на функцията:
input_item = input()
input_day = input()
input_quantity = float(input())

price = calculate_price(input_day, input_item, input_quantity)
print(price)
