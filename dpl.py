import sys
input = sys.stdin.readline


n = int(input())
numbers = [int(x) for x in input().split()]
dp = [[0] * (n + 1) for _ in range(n + 1)]
counter = 0
for j in range(n):
    a = 0
    for i in range(n - j):
        dp[i][j + a] = max(numbers[j + a] - dp[i][j - 1 + a], numbers[i] - dp[i + 1][j + a])
        a += 1
    # print(dp)
print(dp[0][n - 1])
