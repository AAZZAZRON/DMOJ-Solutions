import sys
input = sys.stdin.readline


for _ in range(5):
    amount = int(input())
    n = int(input())
    coins = [int(input()) for _ in range(n)]
    dp = [696969] * (amount + 1)
    dp[0] = 0
    for i in coins:
        for j in range(amount - i + 1):
            if dp[j] != 696969:
                dp[j + i] = min(dp[j + i], dp[j] + 1)
    print(dp[amount])
