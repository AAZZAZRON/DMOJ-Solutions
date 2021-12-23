from sys import stdin
input = stdin.readline


num = int(input())
price = [int(input()) for _ in range(num)]
dp = [0] * (num + 1)
for i in range(num + 1):
    for j in range(num - i):
        dp[i + j + 1] = max(dp[i + j + 1], dp[i] + price[j])
print(dp[-1])
