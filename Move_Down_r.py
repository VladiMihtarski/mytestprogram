def count_unique_paths(m, n):
    # Инициализиране на матрица със стойности 1
    dp = [[1] * n for _ in range(m)]

    # Изчисляване на броя на уникалните пътища
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

# Входни данни
m = int(input())
n = int(input())

# Изчисляване и отпечатване на броя на уникалните пътища
result = count_unique_paths(m, n)
print(result)
