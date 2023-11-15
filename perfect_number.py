def is_perfect_number(number):
    if number <= 0:
        return "It's not so perfect."  # Negative numbers and zero are not perfect

    divisors_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)

    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

# Example usage:
number_to_check = int(input("Enter a number: "))
result = is_perfect_number(number_to_check)
print(result)
