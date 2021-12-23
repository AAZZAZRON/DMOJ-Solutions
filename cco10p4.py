from sys import stdin
input = stdin.readline


num = int(input())
items = [[] for _ in range(num)]
n = int(input())
for _ in range(n):
    a, b, c = [int(x) for x in input().split()]
    items[c - 1].append([a, b])
cost = int(input())
dp = [0] * (cost + 1)
for i in range(num):  # item
    for k in range(cost, -1, -1):  # amount of money
        for a, b in items[i]:  # get item value & cost
            if k >= a:
                dp[k] = max(dp[k], dp[k - a] + b)
print(dp[cost])
