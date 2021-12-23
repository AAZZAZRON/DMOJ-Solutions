num = int(input())
numbers = [0] + [int(x) for x in input().split()]
dp = [0] * (num + 1)
for j in range(1, num + 1):
    dp[j] = max(dp[j], dp[j - 2] + numbers[j], dp[j - 1])
print(dp[-1])
