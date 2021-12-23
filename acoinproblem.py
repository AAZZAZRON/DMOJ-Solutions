from sys import stdin
input = stdin.readline


numCoins, transactions = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]
need = [[] for _ in range(numCoins)]
maximum = 0
answers = [0] * transactions
for i in range(transactions):
    x, y = [int(x) for x in input().split()]
    maximum = max(maximum, x)
    need[y - 1].append([x, i])

prev = [99999] * (maximum + 1)
prev[0] = 0
dp = [99999] * (maximum + 1)

for i in range(1, numCoins + 1):
    coin = coins[i - 1]
    count = 0
    for j in range(maximum + 1):
        if j < coin:
            dp[j] = prev[j]
        else:
            if j % coin == 0:
                count += 1
            dp[j] = min(prev[j], dp[j - coin] + 1)
    for y, pos in need[i - 1]:
        answers[pos] = dp[y]
    # print(dp)
    prev, dp = dp, prev

for i in answers:
    print(i) if i != 99999 else print(-1)
