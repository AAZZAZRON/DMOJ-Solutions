from sys import stdin
input = stdin.readline


nodes, n = [int(x) for x in input().split()]
isEntrance = [1] * nodes
isDest = [1] * nodes
connections = [[] for _ in range(nodes)]
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    isEntrance[b] = 0
    isDest[a] = 0
    connections[a].append(b)
q = [[]]
counter = 0
people = 0
fast = [696969696969] * nodes
for i in range(nodes):
    if isEntrance[i]:
        q[0].append(i)

while q:
    counter += 1
    queued = q.pop()
    added = []
    for node in queued:
        for next in connections[node]:
            if isDest[next]:
                people += 1
                fast[next] = min(fast[next], counter + 1)
            else:
                added.append(next)
    if added:
        q.append(added)
print(people % 1000000007)
print(" ".join([str(x) for x in fast if x != 696969696969]))
