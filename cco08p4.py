from sys import stdin
from collections import deque
input = stdin.readline


r, c = [int(x) for x in input().split()]
grid = [input()[:-1] for _ in range(r)]
visited = [[False] * c for _ in range(r)]
traps = 0
moves = [[1, 0, "N"], [0, 1, "W"], [-1, 0, "S"], [0, -1, "E"]]
for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            traps += 1
            queue = deque([[i, j]])
            visited[i][j] = True
            while queue:
                x, y = queue.pop()
                for a, b, find in moves:
                    a += x
                    b += y
                    if 0 <= a < r and 0 <= b < c and not visited[a][b] and grid[a][b] == find:
                        visited[a][b] = True
                        queue.append([a, b])
                command = grid[x][y]
                if command == "N":
                    x -= 1
                elif command == "E":
                    y += 1
                elif command == "S":
                    x += 1
                elif command == "W":
                    y -= 1
                if not visited[x][y]:
                    visited[x][y] = True
                    queue.append([x, y])
print(traps)
