from sys import stdin
input = stdin.readline


num, maximum = map(int, input().split())
dp = [0] * (maximum + 1)
for _ in range(num):
    weight, val = map(int, input().split())
    for j in range(maximum, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + val)
print(dp[maximum])
