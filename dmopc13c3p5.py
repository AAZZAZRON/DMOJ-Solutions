import sys
input = sys.stdin.readline


mins, cap, n = [int(x) for x in input().split()]
dp = [[-1] * (cap + 1) for _ in range(mins + 1)]
# let dp[i][j] be the max happiness
# from eating j units of food
# spending i minutes
dp[0][0] = 0
maximum = 0
for _ in range(n):
    val, time, food = [int(x) for x in input().split()]
    for i in range(mins - time, -1, -1):
        for j in range(cap - food, -1, -1):
            if dp[i][j] != -1:
                dp[i + time][j + food] = max(dp[i + time][j + food], dp[i][j] + val)
                maximum = max(maximum, dp[i + time][j + food])
# [print(x) for x in dp]
print(maximum)
