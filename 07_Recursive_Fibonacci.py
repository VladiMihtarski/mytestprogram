def getFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return getFibonacci(n-1) + getFibonacci(n-2)

# Четене на входното число
n = int(input())

# Изчисляване на (n+1)-вото число на Фибоначи
fibonacci_number = getFibonacci(n + 1)

# Извеждане на резултата
print(fibonacci_number)
