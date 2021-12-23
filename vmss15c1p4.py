from sys import stdin
import heapq
input = stdin.readline


maxK, nB, nR, nS = [int(x) for x in input().split()]
connections = [[999999999] * (nB + 1) for _ in range(nB + 1)]
foodBasics = [int(input()) for _ in range(nS)]
for _ in range(nR):
    a, b, c = [int(x) for x in input().split()]
    connections[a][b] = min(connections[a][b], c)

visited = {0: 0}
queue = [[0, 0]]
path = {}
nodes = set(x for x in range(nB + 1))
while nodes and queue:
    distance, node = heapq.heappop(queue)
    try:
        while node not in nodes:
            distance, node = heapq.heappop(queue)
    except IndexError:
        break
    nodes.remove(node)
    for i in range(nB + 1):
        if connections[node][i] == 999999999:
            continue
        new = distance + connections[node][i]
        if i not in visited or new < visited[i]:
            visited[i] = new
            heapq.heappush(queue, [new, i])
            path[i] = new
# print(path)
counter = 0
for x in foodBasics:
    if x in path and path[x] <= maxK:
        counter += 1
print(counter)
