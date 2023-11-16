def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def calculate_and_print_division(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        return

    fact_num1 = factorial(num1)
    fact_num2 = factorial(num2)

    division_result = fact_num1 / fact_num2

    formatted_result = "{:.2f}".format(division_result)

    print(f"The factorial of {num1} is {fact_num1}.")
    print(f"The factorial of {num2} is {fact_num2}.")
    print(f"The division result formatted to the second decimal point is: {formatted_result}")


# Example usage:
num1 = int(input("Enter the first integer number: "))
num2 = int(input("Enter the second integer number: "))

calculate_and_print_division(num1, num2)
