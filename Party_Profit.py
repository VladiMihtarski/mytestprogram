def calculate_coins_per_companion(number_of_companions, days):
  """Calculates the number of coins each companion receives, based on the given number of companions and days.

  Args:
    number_of_companions(int): The number of companions.
    days(int): The number of days.

  Returns:
    The number of coins each companion receives.
  """

  coins = 0
  for current_day in range(1, days + 1):
    if current_day % 10 == 0:
      number_of_companions -= 2
    if current_day % 15 == 0:
      number_of_companions += 5
    if current_day % 3 == 0:
      coins -= number_of_companions * 3
    if current_day % 5 == 0:
      coins += number_of_companions * 20
      if current_day % 3 == 0:
        coins -= number_of_companions * 2
    coins += 50
    coins -= number_of_companions * 2

  coins_per_companion = coins // number_of_companions
  return coins_per_companion, number_of_companions


# Get the number of companions and days from the user.
number_of_companions = int(input("Enter the number of companions: "))
days = int(input("Enter the number of days: "))

# Calculate the number of coins each companion receives.
coins_per_companion, number_of_companions = calculate_coins_per_companion(number_of_companions, days)

# Print the results.
print(f"{number_of_companions} companions received {coins_per_companion} coins each.")
