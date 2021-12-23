from sys import stdin
input = stdin.readline

dp = [[1] * 2001] + [[0] * 2001 for _ in range(2000)]
for i in range(1, 2001):
    for j in range(i + 1, 2001):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
num = int(input())
for q in range(1, num + 1):
    x, y = [int(x) for x in input().split("-")]
    print(f"Case #{q}: {dp[y][x]} {dp[y][y + 1]}")
