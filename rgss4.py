n = int(input())
numbers = [int(input()) for _ in range(n)] + [0]
# print(numbers)
dp = [1] * n
total = 0
for i in range(n):
    maximum = 0
    for j in range(i):
        if numbers[j] < numbers[i]:
            maximum = max(maximum, dp[j])
    dp[i] = maximum + numbers[i]
    total = max(total, dp[i])
# print(dp)
print(total)
