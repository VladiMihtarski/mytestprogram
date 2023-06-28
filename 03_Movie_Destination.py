costs = [
    ["Winter", "Dubai", 45000],
    ["Winter", "Sofia", 17000],
    ["Winter", "London", 24000],
    ["Summer", "Dubai", 40000],
    ["Summer", "Sofia", 12500],
    ["Summer", "London", 20250]
]

def calculate_total_cost(destination, season, number_of_days, budget):
    # Намиране на дневната цена според сезона и дестинацията
    for cost in costs:
        if cost[0] == season and cost[1] == destination:
            daily_cost = cost[2]
            break
    else:
        # Изпълнява се само ако не е намерена съответна комбинация от сезон и дестинация
        return "Invalid destination or season"

    # Изчисляване на общата цена
    total_cost = daily_cost * number_of_days

    # Прилагане на отстъпки/увеличения върху общата цена според дестинацията
    if destination == "Dubai":
        total_cost *= 0.7  # 30% отстъпка
    elif destination == "Sofia":
        total_cost *= 1.25  # увеличение с 25%

    # Изчисляване на разликата между бюджета и общата цена
    difference = abs(budget - total_cost)

    # Проверка дали бюджетът е достатъчен или не
    if budget >= total_cost:
        return f"The budget for the movie is enough! We have {difference:.2f} leva left!"
    else:
        return f"The director needs {difference:.2f} leva more!"


# Въвеждане на данни от потребителя
budget = float(input("Enter the budget: "))
destination = input("Enter the destination: ")
season = input("Enter the season: ")
number_of_days = int(input("Enter the number of days: "))

# Изчисляване на общата цена и отпечатване на резултата
result = calculate_total_cost(destination, season, number_of_days, budget)
print(result)
