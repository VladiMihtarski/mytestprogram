def Ski_holiday (days, type_room, evaluation):

    price_per_night = 0
    discount = 0

    if type_room == "room for one person":
        price_per_night = 18.00
    elif type_room == "apartment":
        price_per_night = 25.00
    elif type_room == "president apartment":
        price_per_night = 35.00

    total_price = (days - 1) * price_per_night

    if days < 10:
        if type_room == "apartment":
            discount = total_price * 0.3
        elif type_room == "president apartment":
            discount = total_price * 0.1
    elif 10 <= days <= 15:
        if type_room == "apartment":
            discount = total_price * 0.35
        elif type_room == "president apartment":
            discount = total_price * 0.15
    elif days > 15:
        if type_room == "apartment":
            discount = total_price * 0.5
        elif type_room == "president apartment":
            discount = total_price * 0.2

    total_price -= discount

    if evaluation == "positive":
        total_price += total_price * 0.25
    elif evaluation == "negative":
        total_price -= total_price * 0.1

    print(f"{total_price:.2f}")

input_days = int(input())
input_type_room = input()
input_evaluation = input()
Ski_holiday(input_days, input_type_room, input_evaluation)
