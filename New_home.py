def new_home(kind_of_flowers, pcs_flowers, budget):
    flowers_and_price = {'Roses': 5, 'Dahlias': 3.80, 'Tulips': 2.80, 'Narcissus': 3, 'Gladiolus': 2.50}

    discount = 0
    price_increase = 0

    if kind_of_flowers == "Roses" and pcs_flowers > 80:
        discount = 0.1

    if kind_of_flowers == "Dahlias" and pcs_flowers > 90:
        discount = 0.15

    if kind_of_flowers == "Tulips" and pcs_flowers > 80:
        discount = 0.15

    if kind_of_flowers == "Narcissus" and pcs_flowers < 120:
        price_increase = 0.15

    if kind_of_flowers == "Gladiolus" and pcs_flowers < 80:
        price_increase = 0.2

    price = flowers_and_price[kind_of_flowers] * pcs_flowers * (1 - discount) * (1 + price_increase)


    if budget >= price:
        remaining_amount = budget - price
        print(f"Hey, you have a great garden with {pcs_flowers} {kind_of_flowers} and {remaining_amount:.2f} leva left.")
    else:
        needed_amount = price - budget
        print(f"Not enough money, you need {needed_amount:.2f} leva more.")

input_kind_of_flowers = input()
input_pcs_flowers = int(input())
input_budget = int(input())
new_home(input_kind_of_flowers, input_pcs_flowers, input_budget)
