def pokemon_dont_go(sequence):
    removed_elements_sum = 0

    while sequence:
        index = int(input())

        if index < 0:
            removed_element = sequence.pop(0)
            sequence.insert(0, sequence[-1])
        elif index >= len(sequence):
            removed_element = sequence.pop()
            sequence.append(sequence[0])
        else:
            removed_element = sequence.pop(index)

        removed_elements_sum += removed_element

        for i in range(len(sequence)):
            if sequence[i] <= removed_element:
                sequence[i] += removed_element
            else:
                sequence[i] -= removed_element

    return removed_elements_sum


# Input sequence
sequence = list(map(int, input().split()))

# Get the sum of removed elements
result = pokemon_dont_go(sequence)

# Output the result
print(result)
