from heapq import heappush, heappop
import sys
input = lambda: sys.stdin.readline()[:-1]


r, c = [int(x) for x in input().split()]
grid = []
for i in range(r):
    grid.append([0 if x == "." else 1 for x in input()])
q = [[grid[0][0], 0, 0]]
minimum = [[69696969] * c for _ in range(r)]
minimum[0][0] = grid[0][0]
vis = [[0] * c for _ in range(r)]
vis[0][0] = 1
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
while q:
    v, a, b = heappop(q)
    if v != minimum[a][b]:
        continue
    for x, y in moves:
        x += a
        y += b
        if 0 <= x < r and 0 <= y < c and not vis[x][y] and v + grid[x][y] < minimum[x][y]:
            vis[x][y] = 1
            minimum[x][y] = v + grid[x][y]
            heappush(q, [minimum[x][y], x, y])
print(minimum[r - 1][c - 1])