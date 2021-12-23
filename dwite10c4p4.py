from sys import stdin
input = stdin.readline


moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for q in range(5):
    visited = [[False] * 10 for _ in range(10)]
    queue = []
    added = []
    grid = []
    for x in range(10):
        visited[x][0] = True
        line = [int(x) for x in input()[:-1]]
        grid.append(line)
        added.append([x, 0])
    queue.append(added)
    counter = 0
    done = False
    while queue and not done:
        counter += 1
        added = []
        queued = queue.pop()
        for i, j in queued:
            for x, y in moves:
                x += i
                y += j
                if 0 <= x < 10 and 0 <= y < 10 and not visited[x][y] and abs(grid[i][j] - grid[x][y]) <= 1:
                    visited[x][y] = True
                    added.append([x, y])
                    if y == 9:
                        done = True
        if added:
            queue.append(added)
    if done:
        print(counter)
    else:
        print("IMPOSSIBLE")
    if q != 4:
        tmp = input()
