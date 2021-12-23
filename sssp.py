import sys
from collections import deque
input = sys.stdin.readline


n, m = [int(x) for x in input().split()]
connections = [[0] * (n + 1) for _ in range(n + 1)]
dist = [69696969] * (n + 1)
dist[1] = 0
for _ in range(m):
    a, b, w = [int(x) for x in input().split()]
    if connections[a][b]:
        connections[a][b] = min(connections[a][b], w)
        connections[b][a] = min(connections[b][a], w)
    else:
        connections[a][b] = w
        connections[b][a] = w

q = deque([1])
while q:
    node = q.popleft()
    for j in range(1, n + 1):
        if connections[node][j]:
            if dist[node] + connections[node][j] < dist[j]:
                dist[j] = dist[node] + connections[node][j]
                q.append(j)
[print(x) if x != 69696969 else print(-1) for x in dist[1:]]
