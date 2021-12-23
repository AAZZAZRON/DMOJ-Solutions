from sys import stdin
input = stdin.readline


r, c = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for i in range(r)]
small = [-1] * (c + 1)
dp = [small.copy() for _ in range(r + 1)]
for i in range(1, r + 1):
    for j in range(1, c + 1):
        if dp[i - 1][j] == -1 == dp[i][j - 1]:
            dp[i][j] = grid[i - 1][j - 1]
        elif dp[i - 1][j] == -1:
            dp[i][j] = dp[i][j - 1] + grid[i - 1][j - 1]
        elif dp[i][j - 1] == -1:
            dp[i][j] = dp[i - 1][j] + grid[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
print(dp[-1][-1])
