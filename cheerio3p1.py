n, m = map(int, input().split())
grid = [[x for x in input()] for _ in range(n)]
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for a in range(n):
    for b in range(m):
        if grid[a][b] == "W":
            for x, y in moves:
                x += a
                y += b
                if 0 <= x < n and 0 <= y < m and grid[x][y] != "W":
                    grid[x][y] = "C"
[print("".join(x)) for x in grid]