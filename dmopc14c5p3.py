n = int(input())
numbers = [int(x) for x in input().split()]
dp = [1] * n
for i in range(1, n):
    if abs(numbers[i] - numbers[i - 1]) <= 2:
        dp[i] = dp[i - 1] + 1
print(max(dp))
