def hotel_room(month, nights):
    studio_price = 0
    apartment_price = 0

    if month == "May" or month == "October":
        studio_price = 50
        apartment_price = 65
        if nights > 14:
            studio_price *= 0.7
            apartment_price *= 0.9
        elif nights > 7:
            studio_price *= 0.95
    elif month == "June" or month == "September":
        studio_price = 75.20
        apartment_price = 68.70
        if nights > 14:
            studio_price *= 0.8
            apartment_price *= 0.9
    elif month == "July" or month == "August":
        studio_price = 76
        apartment_price = 77
        if nights > 14:
            apartment_price *= 0.9

    studio_total_price = studio_price * nights
    apartment_total_price = apartment_price * nights

    print(f"Apartment: {apartment_total_price:.2f} lv.")
    print(f"Studio: {studio_total_price:.2f} lv.")

input_month = input()
input_nights = int(input())
hotel_room(input_month, input_nights)
