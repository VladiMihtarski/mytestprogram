# Функция за разпределение и изчисление на сумите за просяците
def calculate_offers(numbers, num_beggars):
    beggars_sums = [0] * num_beggars  # Създаваме списък с нули за всеки просяк

    for i in range(len(numbers)):
        beggar_index = i % num_beggars  # Определяме индекса на текущия просяк
        beggars_sums[beggar_index] += numbers[i]  # Добавяме текущото число към сумата на съответния просяк

    return beggars_sums

# Основна част на програмата
if __name__ == "__main__":
    numbers_input = input("Въведете числата, разделени със запетая и интервал: ")
    # Използваме map и list за конверсия на входните данни към цели числа
    numbers = list(map(int, numbers_input.split(", ")))

    num_beggars = int(input("Въведете брой просяци: "))

    beggars_sums = calculate_offers(numbers, num_beggars)

    print("Сумите за просяците са:", beggars_sums)
