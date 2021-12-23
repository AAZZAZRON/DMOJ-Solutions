from sys import stdin
from collections import deque
input = stdin.readline


moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for _ in range(int(input())):
    length = int(input())
    grid = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            grid[i][j] = int(input())
    high = grid[0][0]
    visited = [[False] * length for _ in range(length)]
    visited[0][0] = True
    queue = deque([[0, 0, 0]])
    done = False
    while queue:
        a, b, oxy = queue.popleft()
        if a == b == length - 1:
            print(oxy)
            done = True
            break
        for x, y in moves:
            x += a
            y += b
            if 0 <= x < length and 0 <= y < length and abs(grid[a][b] - grid[x][y]) <= 2 and not visited[x][y]:
                visited[x][y] = True
                if grid[x][y] > high or grid[a][b] > high:
                    queue.append([x, y, oxy + 1])
                else:
                    queue.append([x, y, oxy])
    if not done:
        print("CANNOT MAKE THE TRIP")
