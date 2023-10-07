def calculate_cost_and_spirit(quantity_of_decorations, remaining_days):
    """Calculates the total cost and total gained spirit for decorating the house for Christmas,
    based on the following constraints:

    * On days that are multiples of 11, you must buy 2 additional decorations.
    * On even days, you buy ornament sets at a cost of 2 per set, and gain 5 spirit points.
    * On days that are multiples of 3, you buy tree skirts and garlands at a cost of 5 and 3 coins, respectively, and gain 10 and 3 spirit points, respectively.
    * On days that are multiples of 5, you buy tree lights at a cost of 15 coins, and gain 17 spirit points. If the day is also a multiple of 3, you gain an additional 30 spirit points.
    * On days that are multiples of 10, the cat ruins all tree decorations, and you lose 20 spirit points. You also go shopping to buy one piece of tree skirt, garlands, and lights, but you do NOT earn additional spirit points for them.

    Args:
        quantity_of_decorations: The quantity of decorations to buy each time you go shopping.
        remaining_days: The number of days left until Christmas.

    Returns:
        A tuple of two integers, representing the total cost and the total gained spirit, respectively.
    """

    total_cost = 0
    total_spirit = 0

    for current_day in range(1, remaining_days + 1):

        # Check if it's a day to add 2 decorations.
        if current_day % 11 == 0:
            quantity_of_decorations += 2

        # Calculate the cost for ornaments on even days.
        if current_day % 2 == 0:
            total_cost += quantity_of_decorations * 2
            total_spirit += 5

        # Calculate the cost for tree skirt and garland on days divisible by 3.
        if current_day % 3 == 0:
            total_cost += quantity_of_decorations * (5 + 3)
            total_spirit += 10 + 3

        # Calculate the cost for tree lights on days divisible by 5.
        if current_day % 5 == 0:
            total_cost += quantity_of_decorations * 15
            total_spirit += 17

            # Additional cost if also divisible by 3.
            if current_day % 3 == 0:
                total_spirit += 30

        # Calculate the cost for special items on days divisible by 10.
        if current_day % 10 == 0:
            total_spirit -= 20
            total_cost += 5 + 3 + 15

    # If the last day is a tenth day, the cat ruins additional items.
    if remaining_days % 10 == 0:
        total_spirit -= 30

    return total_cost, total_spirit


# Get the quantity of decorations and remaining days from the user.
quantity_of_decorations = int(input())
remaining_days = int(input())

# Calculate the total cost and total spirit.
total_cost, total_spirit = calculate_cost_and_spirit(quantity_of_decorations, remaining_days)

# Print the results.
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
