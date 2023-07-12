fibonacci_cache = {}


def getFibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 0:
        fibonacci_cache[n] = 0
    elif n == 1:
        fibonacci_cache[n] = 1
    else:
        fibonacci_cache[n] = getFibonacci(n - 1) + getFibonacci(n - 2)

    return fibonacci_cache[n]


# Четене на входното число
n = int(input())

# Изчисляване на n-тото число на Фибоначи
fibonacci_number = getFibonacci(n+1)

# Извеждане на резултата
print(fibonacci_number)
