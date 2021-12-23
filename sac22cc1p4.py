import sys
input = sys.stdin.readline

n = int(input())
MAX = 101
arr = [int(x) for x in input().split()]

# let dp[x][y][z] be the number of ways to make z
# with y values, ending at ind x
# dp[n + 1][3][101]
dp = [[0] * (MAX + 1) for _ in range(4)]
dp[0][0] = 1
total = 0
for i in range(1, n + 1):
    v = arr[i - 1]
    total += dp[3][v]
    for j in range(MAX - 1, -1, -1):
        for k in range(2, -1, -1):
            dp[k + 1][min(MAX, j + v)] += dp[k][j]
    # print(dp)

print(total)
