t = int(input())
MOD = 1000000007
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    need = [0] * (n + 1)
    # let dp[i][j] be the # ways to feed first i foxes
    # with j crackers
    dp = [[0] * 201 for _ in range(201)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        a, b = [int(x) for x in input().split()]
        m -= a
        need[i] = b - a
    for i in range(1, n + 1):
        slide = 0
        for j in range(min(m, need[i]) + 1):
            slide = (slide + dp[i - 1][j]) % MOD
            dp[i][j] = slide
        for j in range(min(m, need[i]) + 1, m + 1):
            slide = (slide - dp[i - 1][j - need[i] - 1] + dp[i - 1][j] + MOD) % MOD
            dp[i][j] = slide
    print(dp[n][m])
