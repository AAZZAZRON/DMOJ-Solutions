from sys import stdin
from collections import deque
input = stdin.readline


nodes, path = [int(x) for x in input().split()]
connections = [[] for _ in range(nodes + 1)]
minimum = [[9999999999, 9999999999] for _ in range(nodes + 1)]
for _ in range(path):
    x, y, cost = [int(a) for a in input().split()]
    connections[x].append([y, cost])
    connections[y].append([x, cost])
queue = deque([[1, 0]])
while queue:
    a, cost = queue.popleft()
    for node, added in connections[a]:
        if cost + added < minimum[node][1] and cost + added != minimum[node][0]:
            del minimum[node][1]
            minimum[node].append(cost + added)
            minimum[node].sort()
            queue.append([node, cost + added])
print(minimum[nodes][1])
