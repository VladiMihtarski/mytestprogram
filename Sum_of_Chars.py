def sum_ascii_codes(n: int) -> None:
    """
    Calculate the sum of ASCII codes for a given number of characters.

    Args:
        n (int): The number of characters to process.
    """
    total_sum = 0

    for i in range(n):
        char = input()
        char_code = ord(char)
        total_sum += char_code

    print(f"The sum of ASCII codes equals: {total_sum}")

# Input the number of characters
n = int(input())
sum_ascii_codes(n)
