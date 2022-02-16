import heapq


n, m = [int(x) for x in input().split()]
conn = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = [int(x) for x in input().split()]
    conn[a].append([b, c])
    conn[b].append([a, c])

minD = [[69696969, 69696969] for _ in range(n + 1)]
vis = [0] * (n + 1)
vis[1] = 1
minD[1] = [0, 0]
pq = [[0, 0, 1]]
while pq:
    danger, dist, node = heapq.heappop(pq)
    if minD[node] != [danger, dist]:
        continue
    for nex, dg in conn[node]:
        if not vis[nex]:
            if danger + dg < minD[nex][0]:
                minD[nex] = [danger + dg, dist + 1]
                heapq.heappush(pq, minD[nex] + [nex])
            elif danger + dg == minD[nex][0] and dist + 1 < minD[nex][1]:
                minD[nex] = [danger + dg, dist + 1]
                heapq.heappush(pq, minD[nex] + [nex])
    vis[node] = 1
if minD[n][0] != 69696969:
    print(minD[n][0], minD[n][1])
else:
    print(-1)
