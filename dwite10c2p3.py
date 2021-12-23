for q in range(5):
    grid = []
    for _ in range(8):
        line = input()
        a = []
        for i in line:
            if i in "123456789":
                a.append(int(i))
            elif i == ".":
                a.append(0)
            else:
                a.append(-1)
        grid.append(a)
    dp = [[0] * 8 for _ in range(9)]
    dp[7][0] = grid[7][0]
    for i in range(7, -1, -1):
        for j in range(8):
            if grid[i][j] != -1:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                dp[i][j] += grid[i][j]
    print(dp[0][7])
    if q != 4:
        l = input()
