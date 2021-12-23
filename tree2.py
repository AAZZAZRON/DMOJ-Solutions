import sys
from math import sqrt
from collections import deque
input = sys.stdin.readline


r, c = [int(x) for x in input().split()]
grid = []
sX, sY = 0, 0
# initialize board
for a in range(r):
    line = input().split()
    for i in range(c):
        if line[i] == ".":
            line[i] = 0
        elif line[i] == "X":
            line[i] = 0
            sX = a
            sY = i
        else:
            line[i] = int(line[i])
    grid.append(line)
# print(" ".join("".join(str(j) for j in grid[i]) for i in range(r)))
# find biggest tree that is closes to start
maximum = 0
dist = 100
endX, endY = 0, 0
for i in range(r):
    for j in range(c):
        if grid[i][j] > maximum:
            maximum = grid[i][j]
            dist = sqrt((i - sX) ** 2 + (j - sY) ** 2)
            endX = i
            endY = j
        elif grid[i][j] == maximum:
            if sqrt((i - sX) ** 2 + (j - sY) ** 2) < dist:
                dist = sqrt((i - sX) ** 2 + (j - sY) ** 2)
                endX = i
                endY = j
# print(maximum, endX, endY)

# implement BFS
minLength = [[100] * c for _ in range(r)]
cutDown = [[100] * c for _ in range(r)]
queue = deque()
queue.append([sX, sY])
minLength[sX][sY] = 0
grid[endX][endY] = 0
cutDown[sX][sY] = 0
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
while queue:
    a, b = queue.popleft()
    if a == endX and b == endY:
        continue
    for x, y in moves:
        x += a
        y += b
        if 0 <= x < r and 0 <= y < c:
            tmp = minLength[a][b] + grid[x][y]
            addCut = grid[x][y] != 0
            if tmp < minLength[x][y]:
                minLength[x][y] = tmp
                cutDown[x][y] = cutDown[a][b] + addCut
                queue.append([x, y])
            elif tmp == minLength[x][y]:
                if cutDown[a][b] + addCut < cutDown[x][y]:
                    cutDown[x][y] = cutDown[a][b] + addCut
                    queue.append([x, y])
# print(minLength[endX][endY], cutDown[endX][endY])
print(cutDown[endX][endY])
