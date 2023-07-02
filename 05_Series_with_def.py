def apply_discount(series_name, series_price):
    discounts = {
        "Thrones": 0.50,
        "Lucifer": 0.40,
        "Protector": 0.30,
        "TotalDrama": 0.20,
        "Area": 0.10
    }

    if series_name in discounts:
        series_price -= series_price * discounts[series_name]

    return series_price


def main():
    budget = float(input())
    num_series = int(input())

    total_cost = 0

    for _ in range(num_series):
        series_name = input()
        series_price = float(input())

        series_price = apply_discount(series_name, series_price)

        total_cost += series_price

    if budget >= total_cost:
        remaining_money = budget - total_cost
        print(f"You bought all the series and left with {remaining_money:.2f} lv.")
    else:
        needed_money = total_cost - budget
        print(f"You need {needed_money:.2f} lv. more to buy the series!")


if __name__ == "__main__":
    main()
