from sys import stdin
input = stdin.readline


for q in range(5):
    cap = int(input())
    num = int(input())
    records = [[int(x) for x in input().split()] for _ in range(num)]
    prev = [0] * (cap + 1)
    dp = prev.copy()
    for i in range(1, num + 1):
        weight, points = records[i - 1]
        for j in range(1, cap + 1):
            if j < weight:
                dp[j] = prev[j]
            else:
                dp[j] = max(prev[j], prev[j - weight] + points)
        dp, prev = prev, dp

    print(prev[-1])
    if q < 4:
        blank = input()
