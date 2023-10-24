# Въвеждане на последователност от числа разделени с интервали
input_sequence = input("Въведете последователност от числа: ")
numbers = list(map(int, input_sequence.split()))

# Функция за проверка дали число е четно
def is_even(number):
    return number % 2 == 0

# Използване на filter() за филтриране на четните числа
even_numbers = list(filter(is_even, numbers))

# Извеждане на резултата
print("Четните числа са:", even_numbers)
