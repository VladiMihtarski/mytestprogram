def calculate_result(num1, num2, num3, num4):
    """
    Calculate the final result based on the provided formula.

    Args:
        num1 (int): The first input number.
        num2 (int): The second input number.
        num3 (int): The third input number.
        num4 (int): The fourth input number.

    Returns:
        int: The final result.
    """
    result = (num1 + num2) // num3 * num4
    return result

# Input four numbers from the user.
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# Calculate the final result.
result = calculate_result(num1, num2, num3, num4)

# Print the final result.
print(result)
