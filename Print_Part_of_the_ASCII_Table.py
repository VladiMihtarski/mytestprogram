def print_ascii_range(start_index, end_index):
    """
    Print characters from the ASCII table within the specified range.

    Args:
        start_index (int): The index to start printing from.
        end_index (int): The index to stop printing at.
    """
    for i in range(start_index, end_index + 1):
        print(chr(i), end=" ")  # Print the character with a space separator

# Input the start and end indices
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

# Call the function to print the characters
print_ascii_range(start_index, end_index)
