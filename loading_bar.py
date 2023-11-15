def generate_loading_bar(number):
    if number == 100:
        loading_bar = f"{number}% Complete!\n[{'%' * 10}]"
    elif 0 <= number <= 100 and number % 10 == 0:
        num_blocks = number // 10
        percentage = number
        loading_bar = f"{percentage}% [{'%' * num_blocks}{'.' * (10 - num_blocks)}]"
    else:
        return "Invalid input. Please enter a number between 0 and 100 divisible by 10."

    return loading_bar

# Example usage:
input_number = int(input("Enter a number (divisible by 10 between 0 and 100): "))
result = generate_loading_bar(input_number)
print(result)

# Example for still loading
if input_number < 100:
    print("Still loading...")
