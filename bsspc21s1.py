n, m = [int(x) for x in input().split()]
grid = [[x for x in input()] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == "." and grid[i][j] != grid[-(i + 1)][j]:
            grid[i][j] = grid[-(i + 1)][j]
        if grid[i][j] == "." and grid[i][j] != grid[i][-(j + 1)]:
            grid[i][j] = grid[i][-(j + 1)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == "." and grid[i][j] != grid[-(i + 1)][j]:
            grid[i][j] = grid[-(i + 1)][j]
        if grid[i][j] == "." and grid[i][j] != grid[i][-(j + 1)]:
            grid[i][j] = grid[i][-(j + 1)]
bad = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] != grid[-(i + 1)][j]:
            bad = 1
        if grid[i][j] != grid[i][-(j + 1)]:
            bad = 1
        # print(i, j, -(i + 1), j, i, -(j + 1))
if bad:
    print(-1)
else:
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                grid[i][j] = "a"
    [print("".join(x)) for x in grid]
