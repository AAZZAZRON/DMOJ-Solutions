import sys
input = lambda: sys.stdin.readline()[:-1]

n, m = [int(x) for x in input().split()]
visited = [[0] * m for _ in range(n)]
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
grid = []
queue = []
one, two = 0, 0
for i in range(n):
    line = input()
    if "s" in line:
        ind = line.index("s")
        queue.append([[i, ind]])
        visited[i][ind] = 1
    if "e" in line:
        one, two = i, line.index("e")
    grid.append(line)

counter = 0
while queue:
    counter += 1
    queued = queue.pop()
    added = []
    for a, b in queued:
        for x, y in moves:
            x += a
            y += b
            if 0 <= x < n and 0 <= y < m and not visited[x][y] and grid[x][y] != "X":
                visited[x][y] = 1
                if x == one and y == two:
                    print(counter - 1)
                    sys.exit()
                added.append([x, y])
    if added:
        queue.append(added)

print(-1)
