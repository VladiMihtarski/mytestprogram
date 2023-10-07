def calculate_easter_bread_loaves(budget, flour_price):
  """Calculates how many loaves of Easter bread you can make, the colored eggs you have collected, and the money you have left, according to the recipe provided.

  Args:
    budget: The budget you have, in BGN float.
    flour_price: The price for 1 kg flour, in BGN float.

  Returns:
    A tuple of three floats, representing the number of loaves of Easter bread you have made, the colored eggs you have collected, and the money you have left, respectively.
  """

  # Calculate the price for 1 pack of eggs and 1 liter of milk.
  egg_price = flour_price * 0.75
  milk_price = flour_price * 1.25

  # Calculate the total cost of one loaf of Easter bread.
  loaf_cost = egg_price + flour_price + (milk_price * 0.25)

  # Initialize the variables to track the number of loaves made, the number of colored eggs collected, and the remaining budget.
  loaves_made = 0
  colored_eggs = 0
  remaining_budget = budget

  # While the remaining budget is greater than the cost of one loaf of bread, keep making loaves.
  while remaining_budget >= loaf_cost:

    # Make a loaf of bread.
    loaves_made += 1

    # Collect 3 colored eggs for making the loaf of bread.
    colored_eggs += 3

    # Subtract the cost of the loaf from the remaining budget.
    remaining_budget -= loaf_cost

    # Every 3rd loaf, you lose some of your colored eggs.
    if loaves_made % 3 == 0:
      colored_eggs -= (loaves_made - 2)

  return loaves_made, colored_eggs, remaining_budget


# Example usage:

budget = float(input())
flour_price = float(input())

loaves_made, colored_eggs, remaining_budget = calculate_easter_bread_loaves(budget, flour_price)

print(f"You made {loaves_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {remaining_budget:.2f}BGN left.")
