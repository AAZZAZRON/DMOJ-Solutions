n, m = [int(x) for x in input().split()]
MOD = 1000000007

# let dp[i][0] be max ending with blue
# let dp[i][1] be max, ending with red
# let dp[i][2] be max, ending with yellow
dp = [[0, 0, 0] for _ in range(m)]
dp[0] = [1, 1, 1]
for i in range(1, m):
    dp[i][0] = (dp[i - 1][2] + dp[i - 1][0]) % MOD
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][1]) % MOD
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD

# [print(x) for x in dp]
ans = pow(sum(dp[m - 1]), n, MOD)
print(ans)
