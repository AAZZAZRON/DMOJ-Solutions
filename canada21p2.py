import sys
input = sys.stdin.readline


n, q = [int(x) for x in input().split()]
moves = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
graph = [[[0] * 101 for _ in range(101)] for _ in range(101)]
visited = [[[0] * 101 for _ in range(101)] for _ in range(101)]
queue = [[]]
for i in range(n):
    a, b, c = [int(x) for x in input().split()]
    graph[a][b][c] = i + 1
    queue[0].append([a, b, c])
    visited[a][b][c] = 1

counter = 1
while queue:
    counter += 1
    queued = queue.pop()
    added = []
    for a, b, c in queued:
        for x, y, z in moves:
            x += a
            y += b
            z += c
            if 0 <= x <= 100 and 0 <= y <= 100 and 0 <= z <= 100:
                if visited[x][y][z] == 0:
                    visited[x][y][z] = counter
                    added.append([x, y, z])
                    graph[x][y][z] = graph[a][b][c]
                elif visited[x][y][z] == counter:
                    graph[x][y][z] = min(graph[x][y][z], graph[a][b][c])
    if added:
        queue.append(added)


for _ in range(q):
    a, b, c = [int(x) for x in input().split()]
    print(graph[a][b][c])
