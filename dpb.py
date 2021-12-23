num, k = [int(x) for x in input().split()]
cost = [0]
cost.extend([int(x) for x in input().split()])
dp = [999999999999] * (num + k + 1)
dp[1] = 0
for i in range(1, num + 1):
    moved = False
    for x in range(1, k + 1):
        if i + x < num + 1:
            dp[i + x] = min(dp[i + x], dp[i] + abs(cost[i + x] - cost[i]))
            moved = True
    if not moved:
        break
    print(dp)
print(dp[-k - 1])
