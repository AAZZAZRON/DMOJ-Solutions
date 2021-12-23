from sys import stdin
input = stdin.readline


num = int(input())
timeTillDeath = [[] for _ in range(1001)]
for _ in range(num):
    a, b, c = [int(x) for x in input().split()]
    timeTillDeath[c].append([a, b])

dp = [0] * 1001
maximum = 0
for i in range(1001):
    for points, time in timeTillDeath[i]:
        for j in range(i, -1, -1):
            if j - time < 0:
                break
            dp[j] = max(dp[j], dp[j - time] + points)
            maximum = max(maximum, dp[j])
print(maximum)
