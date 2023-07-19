def find_index(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1

array = input().split()
element = input()

index = find_index(array, element)
print(index)
