from math import inf

def matrix(n: int, m: int, default):
    return [[default for _ in range(m)] for _ in range(n)]

def charging(n: int, m: int, values: list[int]) -> tuple[int, str]:
    if m == n:
        return (0, " ".join(map(str, values)))
    
    values.sort()
    
    dist = matrix(n + 1, n + 1, 0)
    for i in range(n):
        for j in range(i, n):
            median_house = values[(i + j) // 2]
            dist[i + 1][j + 1] = sum(abs(values[k] - median_house) for k in range(i, j + 1))

    dp = matrix(n + 1, m + 1, inf)
    dp[0][0] = 0
    prev = matrix(n + 1, m + 1, 0)  

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            for k in range(1, i + 1):
                new_dist = dp[k - 1][j - 1] + dist[k][i]
                if new_dist < dp[i][j]:
                    dp[i][j] = new_dist
                    prev[i][j] = k  

    total_sum = dp[n][m]

    result = []
    current_dep = n
    current_station = m

    while current_station > 0:
        k = prev[current_dep][current_station]
        median_house = values[(k + current_dep - 1) // 2]
        result.append(median_house)
        current_dep = k - 1
        current_station -= 1

    result.sort()
    return (total_sum, " ".join(map(str, result)))

first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))

res = charging(first_row[0], first_row[1], second_row)
print(res[0])
print(res[1])