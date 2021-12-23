import sys
input = lambda: sys.stdin.readline()[:-1]


def findNextHider(sX, sY, found, fCount=0):
    global hide
    if fCount == hide:
        return 0
    visited = [[0] * c for _ in range(r)]
    visited[sX][sY] = 1
    queue = [[[sX, sY]]]
    counter = 0
    final = 696969
    while queue:
        counter += 1
        queued = queue.pop()
        added = []
        for a, b in queued:
            for x, y in moves:
                x += a
                y += b
                if 0 <= x < r and 0 <= y < c and not visited[x][y] and grid[x][y] != "X":
                    visited[x][y] = 1
                    added.append([x, y])
                    if grid[x][y] == "H" and (x, y) not in found:
                        tmp = found.copy()
                        tmp.add((x, y))
                        final = min(final, counter + findNextHider(x, y, tmp, fCount + 1))
        if added:
            queue.append(added)
    return final


r, c, hide = [int(x) for x in input().split()]
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
grid = []
start = []
for a in range(r):
    line = input()
    if "G" in line:
        start = [a, line.index("G")]
    grid.append(line)
print(findNextHider(start[0], start[1], set()))
