import sys
input = sys.stdin.readline


dp = [0] * 256
for _ in range(5):
    one = input()[:-1]
    two = one[::-1]
    prev = [0] * 256
    length = len(one)
    for i in range(1, length + 1):
        for j in range(1, length + 1):
            if one[i - 1] == two[j - 1]:
                dp[j] = prev[j - 1] + 1
            else:
                dp[j] = max(dp[j - 1], prev[j], prev[j - 1])
        dp, prev = prev, dp
    print(prev[length])

