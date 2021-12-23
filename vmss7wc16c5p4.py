import sys
input = sys.stdin.readline


n = int(input())
values = [int(x) for x in input().split()]
dp = [-1] * (n + 1)
dp[0] = 0
for i in values:
    for j in range(n + 1 - i):
        if dp[j] != -1:
            dp[j + i] = max(dp[j + i], dp[j] + 1)
# print(dp)
print(max(1, dp[n]))
