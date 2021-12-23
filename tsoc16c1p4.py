from sys import stdin
input = stdin.readline


r, c = [int(x) for x in input().split()]
grid = [input()[:-1] for _ in range(r)]
counter = 0
visited = set()
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for x in range(r):
    for y in range(c):
        if grid[x][y] == "M" and (x, y) not in visited:
            # print(x, y)
            counter += 1
            queue = [[x, y]]
            for q, w in queue:
                for a, b in moves:
                    a += q
                    b += w
                    if grid[a][b] != "#" and (a, b) not in visited:
                        queue.append([a, b])
                        visited.add((a, b))
print(counter)
