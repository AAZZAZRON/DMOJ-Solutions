def dsuFind(a):
    root = a
    while parent[root] != root:
        root = parent[root]
    while a != root:
        t = parent[a]
        parent[a] = root
        a = t
    return root


def dsuUnion(a, b):
    f1 = dsuFind(a)
    f2 = dsuFind(b)
    if f1 == f2:
        return 0
    parent[f1] = f2
    return 1


n, q = [int(x) for x in input().split()]
edges = [[int(x) for x in input().split()] for _ in range(q)]
parent = [x for x in range(n + 1)]
total = 0
vals = []
for i in range(q):
    one, two = edges[i]
    if dsuUnion(one, two):
        vals.append(i + 1)
        total += 1
        if total == n - 1:
            break
if total == n - 1:
    [print(x) for x in vals]
else:
    print("Disconnected Graph")
