from sys import stdin
input = stdin.readline


def solve():
    foundStart = False
    visited = set()
    queue = []
    counter = 0
    grid = []
    for x in range(10):
        line = input()[:-1]
        grid.append(line)
        if not foundStart and "X" in line:
            foundStart = True
            start = [x, line.index("X")]
            visited.add(tuple(start))
            queue.append([start])
    while queue:
        counter += 1
        queued = queue.pop()
        added = []
        for a, b in queued:
            for x, y in moves:
                x += a
                y += b
                if 0 <= x < 10 and 0 <= y < 10 and (x, y) not in visited and grid[x][y] != "#":
                    if grid[x][y] == "X":
                        print(counter)
                        return
                    visited.add((x, y))
                    added.append([x, y])
        if added:
            queue.append(added)


moves = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
for q in range(5):
    solve()
    if q != 4:
        passed = input()
