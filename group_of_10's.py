def sort_into_groups(sequence):
    numbers = [(int(num), i) for i, num in enumerate(sequence.split(', '))]
    group_boundary = 10

    while numbers:
        group_numbers = [(num, original_order) for num, original_order in numbers if num <= group_boundary]
        if group_numbers:
            group_numbers.sort(key=lambda x: x[1])
            print(f"Group of {group_boundary}'s: {[num for num, _ in group_numbers]}")
            numbers = [(num, original_order) for num, original_order in numbers if num > group_boundary]
        else:
            print(f"Group of {group_boundary}'s: []")
        group_boundary += 10

# Get input from the user
sequence = input("Enter a sequence of numbers (separated by ', '): ")

# Call the function with user input
sort_into_groups(sequence)
