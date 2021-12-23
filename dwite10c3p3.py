for _ in range(5):
    num = int(input())
    if num % 2 == 1:
        print(0)
    else:
        dp = [0] * (num + 1)
        psa = [0] * (num + 1)
        dp[0] = 1
        for i in range(2, num + 1, 2):
            psa[i] = (psa[i - 2] + 2 * dp[i - 4]) % 1000000
            dp[i] = (dp[i - 2] * 3 + psa[i]) % 1000000
        print(dp[num])
