lenA, lenB = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]
for i in range(1, lenA + 1):
    for j in range(1, lenB + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
