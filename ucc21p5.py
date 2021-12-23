def solve(x1, y1, x2, y2):
    if dp[x1][y1][x2][y2] != 0:
        return dp[x1][y1][x2][y2]
    # option 1
    for i in range(1, x1):
        if solve(i, y1, x1 - i, y1) == -1:
            dp[x1][y1][x2][y2] = 1
            return 1
    for i in range(1, y1):
        if solve(x1, i, x1, y1 - i) == -1:
            dp[x1][y1][x2][y2] = 1
            return 1
    for i in range(1, x2):
        if solve(i, y2, x2 - i, y2) == -1:
            dp[x1][y1][x2][y2] = 1
            return 1
    for i in range(1, y2):
        if solve(x2, i, x2, y2 - i) == -1:
            dp[x1][y1][x2][y2] = 1
            return 1

    # option 2
    for i in range(1, min(11, x1)):
        if solve(x1 - i, y1, x2, y2) == -1:
            dp[x1][y1][x2][y2] = 1
            return 1
    for i in range(1, y1):
        if solve(x1, i, x2, y2) == -1:
            dp[x1][y1][x2][y2] = 1
            return 1
    for i in range(1, min(11, x2)):
        if solve(x1, y1, x2 - i, y2) == -1:
            dp[x1][y1][x2][y2] = 1
            return 1
    for i in range(1, y2):
        if solve(x1, y1, x2, i) == -1:
            dp[x1][y1][x2][y2] = 1
            return 1
    dp[x1][y1][x2][y2] = -1
    return -1


y1, x1, y2, x2 = [int(x) for x in input().split()]
dp = [[[[0] * 3 for _ in range(301)] for _ in range(3)] for _ in range(301)]
dp[1][1][1][1] = -1
if solve(x1, y1, x2, y2) == 1:
    print("W")
else:
    print("L")
