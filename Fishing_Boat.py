def fishing_boat(budget, season, fishermen_pcs):
    seasons = {'Spring': 3000, 'Summer': 4200, 'Autumn': 4200, 'Winter': 2600}

    price = seasons[season]

    if fishermen_pcs <= 6:
        price *= 0.9
    if 7 <= fishermen_pcs <= 11:
        price *= 0.85
    if fishermen_pcs >= 12:
        price *= 0.75

    if fishermen_pcs % 2 == 0 and season != "Autumn":
        price *= 0.95

    if price <= budget:
        money_left = budget - price
        print(f"Yes! You have {money_left:.2f} leva left.")
    else:
        need_money = price - budget
        print(f"Not enough money! You need {need_money:.2f} leva.")

input_budget = int(input())
input_season = input()
input_fishermen_pcs = int(input())
fishing_boat(input_budget, input_season, input_fishermen_pcs)

