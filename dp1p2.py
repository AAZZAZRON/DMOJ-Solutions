import sys
input = sys.stdin.readline


n = int(input())
numbers = [int(input()) for _ in range(n)]
dp = [[0, 0] for _ in range(n + 1)]
prev = dp.copy()
counter = 0
for j in range(0, n):
    for i in range(j, n):
        one = prev[i - 1][1] + numbers[i]
        two = prev[i][1] + numbers[i - j]
        if two > one:
            dp[i] = [two, prev[i][0]]
        elif one == two:
            dp[i] = [one, max(prev[i][0], prev[i - 1][0])]
        else:
            dp[i] = [one, prev[i - 1][0]]
    # print(dp)
    dp, prev = prev, dp
print(prev[n - 1][0])
