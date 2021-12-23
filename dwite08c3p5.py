import sys
input = lambda: sys.stdin.readline()[:-1]

end = []
queue = []
moves = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
for _ in range(5):
    counter = 0
    length = int(input())
    grid = []
    for a in range(length):
        tmp = []
        for b in range(length):
            line = input()
            if "A" in line:
                queue = [[[a, b, line.index("A")]]]
            if "B" in line:
                end = [a, b, line.index("B")]
            tmp.append(line)
        grid.append(tmp)
    visited = [[[0] * length for _ in range(length)] for _ in range(length)]
    done = False
    while not done and queue:
        counter += 1
        queued = queue.pop()
        added = []
        for a, b, c in queued:
            for x, y, z in moves:
                x += a
                y += b
                z += c
                if end[0] == x and end[1] == y and end[2] == z:
                    done = True
                if 0 <= x < length and 0 <= y < length and 0 <= z < length and grid[x][y][z] == '.' and not visited[x][y][z]:
                    visited[x][y][z] = 1
                    added.append([x, y, z])
        if added:
            queue.append(added)
    print(counter)

