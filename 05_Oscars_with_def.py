def calculate_total_points(actor_name, initial_points, num_evaluators):
    total_points = initial_points

    for _ in range(num_evaluators):
        evaluator_name = input()
        evaluator_points = float(input())

        evaluator_length = len(evaluator_name)
        points = evaluator_length * evaluator_points / 2

        total_points += points

        if total_points > 1250.5:
            break

    return total_points


actor_name = input()
initial_points = float(input())
num_evaluators = int(input())

total_points = calculate_total_points(actor_name, initial_points, num_evaluators)

if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name}, you need {needed_points:.1f} more!")
