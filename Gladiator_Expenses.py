def calculate_gladiator_expenses(lost_fights, helmet_price, sword_price, shield_price, armor_price):
    total_helmet_broken = lost_fights // 2
    total_sword_broken = lost_fights // 3
    total_shield_broken = lost_fights // (2 * 3)
    total_armor_broken = total_shield_broken // 2
    expenses = (
        total_helmet_broken * helmet_price
        + total_sword_broken * sword_price
        + total_shield_broken * shield_price
        + total_armor_broken * armor_price
    )
    return expenses

# Read input values
number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

# Calculate expenses using the function
expenses = calculate_gladiator_expenses(number_of_lost_fights, helmet_price, sword_price, shield_price, armor_price)

# Print the total expenses
print(f"Gladiator expenses: {expenses:.2f} aureus")
