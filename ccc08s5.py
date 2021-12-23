from sys import stdin
input = stdin.readline


def solve(a, b, c, d):
    if dp[a][b][c][d] != 0:
        return dp[a][b][c][d]
    if a - 2 >= 0 and b - 1 >= 0 and d - 2 >= 0:
        if solve(a - 2, b - 1, c, d - 2) == -1:
            dp[a][b][c][d] = 1
            return 1
    if a - 1 >= 0 and b - 1 >= 0 and c - 1 >= 0 and d - 1 >= 0:
        if solve(a - 1, b - 1, c - 1, d - 1) == -1:
            dp[a][b][c][d] = 1
            return 1
    if c - 2 >= 0 and d - 1 >= 0:
        if solve(a, b, c - 2, d - 1) == -1:
            dp[a][b][c][d] = 1
            return 1
    if b - 3 >= 0:
        if solve(a, b - 3, c, d) == -1:
            dp[a][b][c][d] = 1
            return 1
    if a - 1 >= 0 and d - 1 >= 0:
        if solve(a - 1, b, c, d - 1) == -1:
            dp[a][b][c][d] = 1
            return 1
    dp[a][b][c][d] = -1
    return -1


dp = [[[[0] * 31 for _ in range(31)] for _ in range(31)] for _ in range(31)]
for _ in range(int(input())):
    a, b, c, d = [int(x) for x in input().split()]
    if solve(a, b, c, d) == 1:
        print("Patrick")
    else:
        print("Roland")
