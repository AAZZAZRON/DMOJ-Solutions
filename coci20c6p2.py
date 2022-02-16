import sys
import heapq
input = sys.stdin.readline


n, m = [int(x) for x in input().split()]
conn = [[] for _ in range(n + 1)]
ids = 1
f = {}
for _ in range(m):
    a, b, c = input().split()
    if a not in f:
        f[a] = ids
        ids += 1
    if b not in f:
        f[b] = ids
        ids += 1
    conn[f[a]].append([f[b], int(c)])
q = []
for _ in range(int(input())):
    a, b = [f[x] for x in input().split()]
    minD = [999999999999999999] * (n + 1)
    minD[a] = 0
    heapq.heappush(q, [0, a])
    while q:
        cost, node = heapq.heappop(q)
        for x, y in conn[node]:
            if cost + y < minD[x]:
                minD[x] = cost + y
                heapq.heappush(q, [minD[x], x])
    print("Roger" if minD[b] == 999999999999999999 else minD[b])
