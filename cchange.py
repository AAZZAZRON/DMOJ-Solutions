from sys import stdin
input = stdin.readline


num = int(input())
dp = [696969] * (num + 1)
dp[0] = 0
for q in range(int(input())):
    i = int(input())
    for j in range(num - i + 1):
        if dp[j] != 696969:
            dp[j + i] = min(dp[j + i], dp[j] + 1)
print(dp[num])
