from sys import stdin
input = stdin.readline


moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for q in range(5):
    trees = 0
    grid = []
    queue = [[]]
    visited = set()
    time = 0
    for a in range(10):
        x = input()[:-1]
        trees += x.count("T")
        grid.append(x)
        ind = 0
        while "F" in x[ind:]:
            index = x[ind:].find("F")
            queue[0].append([a, ind + index])
            visited.add((a, ind + index))
            ind += index + 1
    while queue and trees != 0:
        time += 1
        added = []
        queued = queue.pop()
        for a, b in queued:
            for x, y in moves:
                x += a
                y += b
                if 0 <= x < 10 and 0 <= y < 10 and grid[x][y] == "T" and (x, y) not in visited:
                    visited.add((x, y))
                    added.append([x, y])
                    trees -= 1
        if added:
            queue.append(added)
    if trees == 0:
        print(time)
    else:
        print(-1)
    if q < 4:
        _ = input()
