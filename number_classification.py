# Input numbers separated by comma and space
input_numbers = input("Enter numbers separated by comma and space: ")

# Split the input string into a list of numbers
numbers = [int(num) for num in input_numbers.split(', ')]

# Use list comprehensions to filter positive, negative, even, and odd numbers
positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Format the results as strings
positive_str = ', '.join(map(str, positive_numbers))
negative_str = ', '.join(map(str, negative_numbers))
even_str = ', '.join(map(str, even_numbers))
odd_str = ', '.join(map(str, odd_numbers))

# Print the formatted results
print("Positive:", positive_str)
print("Negative:", negative_str)
print("Even:", even_str)
print("Odd:", odd_str)
