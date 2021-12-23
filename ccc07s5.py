import sys
input = sys.stdin.readline


numCases = int(input())
for q in range(numCases):
    n, b, w = [int(x) for x in input().split()]
    balls = [int(input()) for _ in range(n)] + [0] * w
    window = sum(balls[:w])
    sums = [window]
    for i in range(n - 1):
        window -= balls[i]
        window += balls[i + w]
        sums.append(window)
    # print(sums)
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)
    for q in range(b):
        for i in range(n - 1, -1, -1):
            if i >= n - w:
                dp[i] = sums[i]
            else:
                dp[i] = max(dp[i + 1], prev[i + w] + sums[i])
        prev, dp = dp, prev
    print(prev[0])

