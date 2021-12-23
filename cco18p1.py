from sys import stdin
input = stdin.readline


num = int(input())
aW = input()[:-1]
aP = [int(x) for x in input().split()]
bW = input()[:-1]
bP = [int(x) for x in input().split()]
dp = [[0] * (num + 1) for _ in range(num + 1)]
for i in range(1, num + 1):
    outcome = aW[i - 1]
    points = aP[i - 1]
    for j in range(1, num + 1):
        if outcome != bW[j - 1]:
            if outcome == "W" and points > bP[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + points + bP[j - 1])
            elif outcome == "L" and points < bP[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + points + bP[j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
print(dp[-1][-1])
