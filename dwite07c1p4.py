import sys
input = sys.stdin.readline


height = int(input())
dp = [696969] * (height + 1)
dp[0] = 0
for i in range(int(input())):
    num = int(input())
    for j in range(height - num, -1, -1):
        if dp[j] != 696969:
            dp[j + num] = min(dp[j + num], dp[j] + 1)
print(dp[height]) if dp[height] != 696969 else print(0)
