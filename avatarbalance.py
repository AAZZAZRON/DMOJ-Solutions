num = int(input())
numbers = [int(x) for x in input().split()]
total = sum(numbers)
half = round(total / 2)
dp = [False] * (half + 1)
dp[0] = True
for number in numbers:
    for j in range(half - number, -1, -1):
        if dp[j]:
            dp[j + number] = True
for i in range(half, -1, -1):
    if dp[i]:
        print(abs(total - i - i))
        break
