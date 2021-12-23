from sys import stdin
input = stdin.readline


for q in range(5):
    num = int(input())
    numbers = []
    total = 0
    for _ in range(num):
        x = int(input())
        total += x
        numbers.append(x)
    half = round(total / 2)
    dp = [0] * (half + 1)
    for i in range(num):
        number = numbers[i]
        for j in range(half, number - 1, -1):
            dp[j] = max(dp[j], dp[j - number] + number)
    print(abs(total - 2 * dp[-1]))
