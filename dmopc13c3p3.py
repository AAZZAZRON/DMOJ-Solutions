from collections import deque
from sys import stdin, exit
input = stdin.readline


num, h = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(num)]
visited = [[False] * num for _ in range(num)]
visited[0][0] = True
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
queue = deque()
queue.append([0, 0])
while queue:
    a, b = queue.popleft()
    for x, y in moves:
        x += a
        y += b
        if 0 <= x < num and 0 <= y < num and not visited[x][y] and abs(grid[a][b] - grid[x][y]) <= h:
            queue.append([x, y])
            visited[x][y] = True
    if visited[num - 1][num - 1]:
        print("yes")
        exit()
print("no")
