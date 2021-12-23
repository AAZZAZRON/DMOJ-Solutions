import sys
input = sys.stdin.readline


n, k = [int(x) for x in input().split()]
arr = [0] * (n + 1)
for i in input().split():
    arr[int(i)] += 1
dp = [0] * (k + 1)
prev = dp.copy()
prev[0] = 1
for q in range(1, n + 1):
    dp[0] = prev[0]
    for i in range(1, k + 1):
        dp[i] = prev[i] + arr[q] * prev[i - 1]
    dp, prev = prev, dp
# let dp[i][j] be the number of ways to
# make a boat of size j using the first i fish
print(prev[-1] % 998244353)

