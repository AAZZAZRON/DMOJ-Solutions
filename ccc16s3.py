import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def findConnectedNodes(q):
    edges = [0] * n
    for i in range(n):
        edges[i] = len(adj[i])
    cut = set()
    counter = 0
    while q:
        added = []
        for p in q:
            length = edges[p]
            if length == 1:
                if p not in cut:
                    counter += 1
                    cut.add(p)
                    for check in adj[p]:
                        edges[check] -= 1
                        if check not in cut and check not in pho:
                            added.append(check)
        q, added = added, q
    return cut, counter


def farthestVertex(node):
    maximum = 0
    val = node
    for i in adj[node]:
        if i not in bad and not visited[i]:
            visited[i] = 1
            tmp, f = farthestVertex(i)
            if tmp + 1 > maximum:
                maximum = tmp + 1
                val = f
    return maximum, val


n, m = [int(x) for x in input().split()]
pho = set([int(x) for x in input().split()])
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = [int(x) for x in input().split()]
    adj[a].append(b)
    adj[b].append(a)
if n == 2 and m == 2:
    print(1)
    sys.exit()
queueList = set()
for i in range(n):
    if i not in pho:
        queueList.add(i)
bad, numBad = findConnectedNodes(queueList)
distance = 0
for x in pho:
    visited = [0] * n
    num = farthestVertex(x)[1]
    visited = [0] * n
    distance = farthestVertex(num)[0]
    break
print((n - numBad - 1) * 2 - distance)
