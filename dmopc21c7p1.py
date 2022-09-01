import sys
n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] + [0] for _ in range(n)]
grid.append([0] * (m + 1))
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + 1
        elif grid[i - 1][j] >= grid[i][j] or grid[i][j - 1] >= grid[i][j]:
            print(-1)
            sys.exit()
for i in range(n):
    print(*grid[i][:-1])