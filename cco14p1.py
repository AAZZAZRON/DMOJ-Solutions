from sys import stdin
input = stdin.readline


num = int(input())
grid = [input()[:-1] for _ in range(num)]
dp = [[0] * (num + 2) for _ in range(num + 1)]
counter = 0
for i in range(num - 1, -1, -1):
    for j in range(1, num + 1):
        if grid[i][j - 1] == "#":
            dp[i][j] = min(dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1]) + 1
            counter += dp[i][j]
# [print(x) for x in dp]
print(counter)
