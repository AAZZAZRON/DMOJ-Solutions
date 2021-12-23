from sys import stdin
from collections import deque
input = stdin.readline


r, c = [int(x) for x in input().split()]
grid = [input()[:-1] for _ in range(r)]
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = set()
rooms = 0
for x in range(r):
    for y in range(c):
        if grid[x][y] == "." and (x, y) not in visited:
            rooms += 1
            queue = deque()
            queue.append([x, y])
            visited.add((x, y))
            while queue:
                a, b = queue.popleft()
                for i, j in moves:
                    i += a
                    j += b
                    if 0 <= i < r and 0 <= j < c and grid[i][j] == "." and (i, j) not in visited:
                        visited.add((i, j))
                        queue.append([i, j])
print(rooms)
