r, c = [int(x) for x in input().split()]
grid = [input() for _ in range(r)]
visited = [[0] * c for _ in range(r)]
smallest = grid[0][0]
queued = [[[0, 0]]]
while queued:
    q = queued.pop()
    add = []
    l = "z"
    for x, y in q:
        if x + 1 < r and not visited[x + 1][y]:
            if grid[x + 1][y] < l:
                l = grid[x + 1][y]
                add = [[x + 1, y]]
                visited[x + 1][y] = 1
            elif grid[x + 1][y] == l:
                add.append([x + 1, y])
                visited[x + 1][y] = 1
        if y + 1 < c and not visited[x][y + 1]:
            if grid[x][y + 1] < l:
                l = grid[x][y + 1]
                add = [[x, y + 1]]
                visited[x][y + 1] = 1
            elif grid[x][y + 1] == l:
                add.append([x, y + 1])
                visited[x][y + 1] = 1
    smallest += l
    if add:
        queued.append(add)
print(smallest[:-1])