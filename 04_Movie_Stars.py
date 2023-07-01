def calculate_actor_honorarium(budget):
    remaining_budget = budget

    while True:
        actor_name = input()
        if actor_name == "ACTION":
            break

        if len(actor_name) > 15:
            actor_honorarium = 0.2 * remaining_budget
        else:
            actor_honorarium = float(input())

        if actor_honorarium > remaining_budget:
            return actor_honorarium - remaining_budget

        remaining_budget -= actor_honorarium

    return remaining_budget


budget = float(input())
needed_budget = calculate_actor_honorarium(budget)

if needed_budget > 0:
    print(f"We need {needed_budget:.2f} leva for our actors.")
else:
    print(f"We are left with {abs(needed_budget):.2f} leva.")
