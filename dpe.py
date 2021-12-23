from sys import stdin
input = stdin.readline


num, limit = [int(x) for x in input().split()]
total = 0
items = []
for _ in range(num):
    a, b = [int(x) for x in input().split()]
    total += b
    items.append([a, b])
dp = [99999999999999999] * (total + 1)
dp[0] = 0
for weight, value in items:
    for j in range(total, -1, -1):
        if j < value:
            break
        dp[j] = min(dp[j], dp[j - value] + weight)
for x in range(total, -1, -1):
    if dp[x] <= limit:
        print(x)
        break
