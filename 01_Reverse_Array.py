def reverse_array(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start + 1, end - 1)


def print_array(arr):
    return ' '.join(map(str, arr))


# Пример за използване:
array = input("Въведете масива: ").split()
array = list(map(int, array))

print("Оригинален масив:")
print(print_array(array))

reverse_array(array, 0, len(array) - 1)

print("Обърнат масив:")
print(print_array(array))
