def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

# Примерна функция за тестване
def main():
    num = int(input("Въведете число: "))
    factorial = recursive_factorial(num)
    print("Факториелът на числото е:", factorial)

main()
