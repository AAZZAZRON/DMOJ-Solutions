from collections import deque


def traverse(one, two):
    global r, c
    visited = [[0] * c for _ in range(r)]
    q = deque()
    q.append([one])
    ct = 0
    while q:
        ct += 1
        queue = q.pop()
        added = []
        for a, b in queue:
            for x, y in moves:
                x += a
                y += b
                if 0 <= x < r and 0 <= y < c and \
                        not visited[x][y] and \
                        grid[x][y] != "#" and \
                        not (97 <= ord(grid[x][y]) <= 122):
                    ch = ord(grid[x][y])
                    visited[x][y] = 1
                    if 65 <= ch <= 90:
                        added.append(ascii[ch + 32])
                        visited[ascii[ch + 32][0]][ascii[ch + 32][1]] = 1
                    elif x == two[0] and y == two[1]:
                        return ct
                    else:
                        added.append([x, y])
        if added:
            q.append(added)
    return -1


ascii = [[] for _ in range(128)]
classes = [[] for _ in range(5)]
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

r, c = [int(x) for x in input().split()]
grid = []
for a in range(r):
    line = input()
    for i in range(c):
        if line[i] in "01234":
            classes[int(line[i])] = [a, i]
        elif line[i] != "#" or line[i] != ".":
            ascii[ord(line[i])] = [a, i]
    grid.append(line)
s = 0
for i in range(1, 5):
    tmp = traverse(classes[i - 1], classes[i])
    if tmp == -1:
        s = -1
        break
    s += tmp
print(s)