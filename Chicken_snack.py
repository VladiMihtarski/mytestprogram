def henrys_street_food(amounts, prices):
    food_count = 0

    while amounts and prices:
        money = amounts.pop()
        price = prices[0]

        if money < price:
            prices.pop(0)

        elif money == price:
            prices.pop(0)
            food_count += 1
        elif money > price:
            diff = money - price
            if amounts:
                amounts[-1] += diff
            prices.pop(0)
            food_count += 1

            continue

    if food_count >= 4:
        print(f"Gluttony of the day! Henry ate {food_count} foods.")
    elif food_count > 1:
        print(f"Henry ate: {food_count} foods.")
    elif food_count == 1:
        print(f"Henry ate: {food_count} food.")
    else:
        print("Henry remained hungry.He will try next weekend again.")

# Example usage:
money_sequence = list(map(int, input().split()))
price_sequence = list(map(int, input().split()))

henrys_street_food(money_sequence, price_sequence)
