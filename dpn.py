import sys
input = sys.stdin.readline


n = int(input())
numbers = [int(x) for x in input().split()]
psa = [0]
[psa.append(i + psa[-1]) for i in numbers]
dp = [[0] * (n + 1) for _ in range(n + 1)]
# let dp[i][j] be the minimum cost to combine the slimes from [i, j]
for i in range(2, n + 1):
    for j in range(i, n + 1):
        sX = i - 1
        sY = j - 1
        eX = 1
        eY = j
        minimum = 100000000000000
        while sX != 0:
            minimum = min(minimum, dp[sX][sY] + dp[eX][eY])
            sX -= 1
            sY -= 1
            eX += 1
        dp[i][j] = minimum + psa[j] - psa[j - i]
# print(dp)
print(dp[n][n])
