import sys
input = sys.stdin.readline


n = int(input())
total = 0
provinces = []
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    total += b
    votes = a // 2 + 1
    provinces.append([votes, b])
# let dp[i] be the # votes to earn i points
dp = [99999999999999999] * (total + 1)
dp[0] = 0
for v, p in provinces:
    for i in range(total, p - 1, -1):
        dp[i] = min(dp[i], dp[i - p] + v)
    # print(dp)
print(min(dp[total // 2 + 1:]))
