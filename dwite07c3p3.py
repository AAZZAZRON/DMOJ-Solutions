from sys import stdin
input = stdin.readline


for q in range(5):
    cap = int(input())
    num = int(input())
    songs = [[int(x) for x in input().split()[1:]] for _ in range(num)]
    small = [0] * (cap + 1)
    dp = [small.copy() for _ in range(num + 1)]
    for i in range(1, num + 1):
        rating, weight = songs[i - 1]
        for j in range(1, cap + 1):
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + rating)
    print(dp[-1][-1])
