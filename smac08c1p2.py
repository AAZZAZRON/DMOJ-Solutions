from sys import stdin
from collections import deque
input = stdin.readline


lines = int(input())
blank = input()
grid = []
visited = set()
queue = deque()
gold = 0
moves = [[0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1], [1, 0, 0]]
for x in range(lines):
    layer = []
    for y in range(lines):
        line = input()[:-1]
        if x == 0:
            index = 0
            while "." in line[index:]:
                ind = line[index:].index(".")
                visited.add((x, y, index + ind))
                queue.append([x, y, index + ind])
                index += ind + 1
            index = 0
            while "*" in line[index:]:
                ind = line[index:].index("*")
                visited.add((x, y, index + ind))
                queue.append([x, y, index + ind])
                gold += 1
                index += ind + 1
        layer.append(line)
    grid.append(layer)
    if x != lines - 1:
        blank = input()
# print(queue)
while queue:
    a, b, c = queue.popleft()
    for x, y, z in moves:
        x += a
        y += b
        z += c
        if 0 <= x < lines and 0 <= y < lines and 0 <= z < lines and (x, y, z) not in visited and grid[x][y][z] != "X":
            if grid[x][y][z] == "*":
                gold += 1
            visited.add((x, y, z))
            queue.append([x, y, z])
print(gold)
