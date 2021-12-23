import sys
input = sys.stdin.readline


n, width = [int(x) for x in input().split()]
fish = [int(x) for x in input().split()]
dp = [0] * n
# let dp[i] be the maximum deliciousness of fish [0, i]
for i in range(n):
    if i - width < 0:
        dp[i] = max(fish[:i + 1])
    else:
        dp[i] = max(max(dp[i - width: i]), dp[i - width - 1] + fish[i])
print(dp[-1])
