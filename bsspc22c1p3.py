import sys
input = sys.stdin.readline
n, m, k = [int(x) for x in input().split()]
grid = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = [int(x) for x in input().split()]
    grid[a][b] = -696969
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = a + i
            y = b + j
            if 1 <= x <= n and 1 <= y <= m:
                grid[x][y] += 1
ct = 0
for i in range(n + 1):
    for j in range(m + 1):
        if grid[i][j] >= 3:
            ct += 1
print(ct)
# [print(x) for x in grid]