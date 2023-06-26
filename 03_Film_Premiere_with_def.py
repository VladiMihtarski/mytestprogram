def calculate_price(projection, movie_pack, number_of_tickets):
    prices = {
        ("John Wick", "Drink"): 12,
        ("John Wick", "Popcorn"): 15,
        ("John Wick", "Menu"): 19,
        ("Star Wars", "Drink"): 18,
        ("Star Wars", "Popcorn"): 25,
        ("Star Wars", "Menu"): 30,
        ("Jumanji", "Drink"): 9,
        ("Jumanji", "Popcorn"): 11,
        ("Jumanji", "Menu"): 14,
    }

    price_per_ticket = prices.get((projection, movie_pack))
    if price_per_ticket is not None:
        total_price = number_of_tickets * price_per_ticket
    else:
        total_price = 0

    return total_price


def apply_discounts(projection, number_of_tickets, total_price):
    if projection == "Star Wars" and number_of_tickets >= 4:
        total_price *= 0.7  # 30% отстъпка за поне 4 билета при "Star Wars"
    elif projection == "Jumanji" and number_of_tickets == 2:
        total_price *= 0.85  # 15% отстъпка за точно 2 билета при "Jumanji"

    return total_price


projection = input()
movie_pack = input()
number_of_tickets = int(input())

total_price = calculate_price(projection, movie_pack, number_of_tickets)
total_price = apply_discounts(projection, number_of_tickets, total_price)

# Форматиране и извеждане на крайната цена
formatted_price = "{:.2f}".format(total_price)
print(f"Your bill is {formatted_price} leva.")
