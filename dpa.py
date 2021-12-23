num = int(input())
cost = [0]
cost.extend([int(x) for x in input().split()])
cost.append(0)
cost.append(0)
dp = [999999999999] * (num + 3)
dp[1] = 0
for i in range(1, num + 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(cost[i + 1] - cost[i]))
    dp[i + 2] = min(dp[i + 2], dp[i] + abs(cost[i + 2] - cost[i]))
    # print(dp)
print(dp[-3])
