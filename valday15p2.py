from sys import stdin
input = stdin.readline


num, time = [int(x) for x in input().split()]
dp = [0] * (time + 1)
for _ in range(num):
    n, k = [int(x) for x in input().split()]
    for i in range(time, -1, -1):
        if i < k:
            break
        dp[i] = max(dp[i], dp[i - k] + n)
print(dp[-1])
