def generate_pascal_triangle(height):
    triangle = []
    for i in range(height):
        row = [1] * (i+1)  # генерираме реда със съответната дължина и запълваме с 1
        triangle.append(row)

    for i in range(2, height):
        row = triangle[i]
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

    return triangle

def print_pascal_triangle(triangle):
    max_number_width = len(str(triangle[-1][len(triangle[-1]) // 2]))  # определяме ширината на средното число на последния ред
    height = len(triangle)
    for i in range(height):
        row = triangle[i]
        spaces = " " * (height - i - 1)  # добавяме интервали преди числата
        numbers = " ".join(str(number) for number in row)  # превръщаме числата в низ
        print(spaces + numbers)

height = int(input("Въведете височина на Триъгълника на Паскал: "))
triangle = generate_pascal_triangle(height)
print_pascal_triangle(triangle)
