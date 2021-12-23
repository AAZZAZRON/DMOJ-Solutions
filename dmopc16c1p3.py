numShoes = int(input())
prices = [float(x) for x in input().split()]
dp = [999999.0] * (numShoes + 1)
dp[0] = 0.0
for i in range(1, numShoes + 1):
    if i >= 3:
        discount1 = dp[i - 2] + sum(prices[i - 2: i]) - (min(prices[i - 2: i]) / 2)
        discount2 = dp[i - 3] + sum(prices[i - 3: i]) - min(prices[i - 3: i])
        dp[i] = min(dp[i - 1] + prices[i - 1], discount1, discount2)
    elif i >= 2:
        discount1 = dp[i - 2] + sum(prices[i - 2: i]) - (min(prices[i - 2: i]) / 2)
        dp[i] = min(dp[i - 1] + prices[i - 1], discount1)
    else:
        dp[i] = prices[i - 1]
print(dp[-1])
