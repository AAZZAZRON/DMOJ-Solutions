from sys import stdin
input = stdin.readline


num = int(input())
costs = [int(input()) for _ in range(num)]
dp = [9999999999] * (num + 1)
current = 0
dp[0] = 0

for i in range(num + 1):
    if i + 1 <= num:
        dp[i + 1] = min(dp[i + 1], dp[i] + costs[i])
    if i + 2 <= num:
        dp[i + 2] = min(dp[i + 2], dp[i] + costs[i] + costs[i + 1] - (min(costs[i], costs[i + 1]) // 4))
    if i + 3 <= num:
        dp[i + 3] = min(dp[i + 3], dp[i] + costs[i] + costs[i + 1] + costs[i + 2] - (min(costs[i], costs[i + 1], costs[i + 2]) // 2))
print(dp[-1])
