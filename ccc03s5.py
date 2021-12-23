from sys import stdin
from collections import deque
input = stdin.readline


n, q, d = [int(x) for x in input().split()]
adj = [[] for _ in range(n + 1)]
for _ in range(q):
    a, b, c = [int(x) for x in input().split()]
    adj[a].append([b, c])
    adj[b].append([a, c])
weight = [0] * (n + 1)
weight[1] = 60000
queue = deque([1])
while queue:
    node = queue.popleft()
    m = weight[node]
    for next, w in adj[node]:
        if min(m, w) > weight[next]:
            weight[next] = min(m, w)
            queue.append(next)
minimum = 100001
for _ in range(d):
    minimum = min(minimum, weight[int(input())])
print(minimum)
