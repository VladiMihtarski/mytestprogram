def merge_elements(arr, start_index, end_index):
    start_index = max(0, start_index)
    end_index = min(end_index, len(arr) - 1)
    merged = ''.join(arr[start_index:end_index + 1])
    arr[start_index:end_index + 1] = [merged]
    return arr


def divide_element(arr, index, partitions):
    element = arr[index]
    partition_size = len(element) // partitions
    remainder = len(element) % partitions
    divided = [element[i * partition_size:(i + 1) * partition_size] for i in range(partitions - 1)]
    divided.append(element[(partitions - 1) * partition_size:])
    arr.pop(index)
    arr[index:index] = divided
    return arr


# Read the initial array
initial_array = input().split()

# Process commands
while True:
    command = input()
    if command == "3:1":
        break

    tokens = command.split()
    action = tokens[0]

    if action == "merge":
        start_index, end_index = map(int, tokens[1:])
        initial_array = merge_elements(initial_array, start_index, end_index)

    elif action == "divide":
        index, partitions = map(int, tokens[1:])
        initial_array = divide_element(initial_array, index, partitions)

# Print the result
print(' '.join(initial_array))
