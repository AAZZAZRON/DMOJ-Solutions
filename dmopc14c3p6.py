from sys import stdin
input = stdin.readline

num, time = [int(x) for x in input().split()]
prev = [0] * (time + 2)
dp = [0] * (time + 2)
for _ in range(num):
    prev[-1] = -9999999999

    p1, v1, p2, v2, p3, v3 = [int(x) for x in input().split()]
    for i in range(time + 1):
        dp[i] = max(prev[i], prev[max(-1, i - p1)] + v1, prev[max(-1, i - p2)] + v2, prev[max(-1, i - p3)] + v3)
    prev, dp = dp, prev
print(prev[-2])
