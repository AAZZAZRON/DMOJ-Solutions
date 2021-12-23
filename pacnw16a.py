line = input()
numbers = [ord(x) - ord('a') for x in line] + [-1]
# print(numbers)
length = len(numbers)
dp = [1] * length
total = 0
for i in range(length):
    maximum = 0
    for j in range(i):
        if numbers[j] < numbers[i]:
            maximum = max(maximum, dp[j])
    dp[i] = maximum + 1
    total = max(total, dp[i])
# print(dp)
print(26 - total)
