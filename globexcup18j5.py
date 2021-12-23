import sys
input = sys.stdin.readline


houses, m, q, c = [int(x) for x in input().split()]
roads = [[] for _ in range(houses + 1)]
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    roads[a].append(b)
    roads[b].append(a)
shortest = [696969] * (houses + 1)
# let shortest[i] represent the shortest distance from i to c
shortest[c] = 0
counter = 0
queue = [[c]]
while queue:
    counter += 1
    queued = queue.pop()
    added = []
    for node in queued:
        for new in roads[node]:
            if shortest[new] == 696969:
                shortest[new] = counter
                added.append(new)
    if added:
        queue.append(added)
# print(shortest)
for _ in range(q):
    start, end = [int(x) for x in input().split()]
    if shortest[start] == 696969 or shortest[end] == 696969:
        print("This is a scam!")
    else:
        print(shortest[start] + shortest[end])
