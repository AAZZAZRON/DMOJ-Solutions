import sys
input = sys.stdin.readline


for i in range(5):
    numNums = int(input())
    numbers = [int(input()) for _ in range(numNums)]
    dp = [0] * 1441
    for num in numbers:
        for j in range(1440, -1, -1):
            if j < num:
                break
            dp[j] = max(dp[j], dp[j - num] + num)
    print(1440 - dp[-1])
