def sort_numbers(sequence):
    # Split the input sequence into a list of integers
    numbers = [int(x) for x in sequence.split()]

    # Sort the list in ascending order using the sorted() function
    sorted_numbers = sorted(numbers)

    return sorted_numbers


# Get a sequence of numbers from the user
user_input = input("Enter a sequence of numbers separated by spaces: ")

# Call the sort_numbers function and print the sorted result
sorted_result = sort_numbers(user_input)
print("Sorted numbers:", sorted_result)
