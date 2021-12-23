import sys
from collections import deque
input = lambda: sys.stdin.readline()[:-1]
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
while True:
    c, r = [int(x) for x in input().split()]
    if r == c == -1:
        break
    grid = [input() for _ in range(r)]
    visited = [[0] * 20 for _ in range(20)]
    counter = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] != "0" and not visited[i][j]:
                counter += 1
                visited[i][j] = 1
                queue = deque([[i, j]])
                while queue:
                    a, b = queue.popleft()
                    for x, y in moves:
                        x += a
                        y += b
                        if 0 <= x < r and 0 <= y < c and not visited[x][y] and grid[x][y] != "0":
                            visited[x][y] = 1
                            queue.append([x, y])
    print(counter)
