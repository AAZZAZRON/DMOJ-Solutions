num, price = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]
small = [0] * (price + 1)
dp = [small.copy() for i in range(num + 1)]
dp[0][0] = 1
used = set()
for i in range(1, num + 1):
    coin = coins[i - 1]
    # print(coin)
    for j in range(0, price + 1):
        if j - coin >= 0:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - coin]
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
