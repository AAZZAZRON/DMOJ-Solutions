def dsuFind(one):
    root = one
    while parent[root] != root:
        root = parent[root]
    while parent[one] != root:
        t = parent[one]
        parent[one] = root
        one = t
    return root


def dsuUnion(one, two):
    f1 = dsuFind(one)
    f2 = dsuFind(two)
    if f1 == f2:
        return 0
    parent[f1] = f2
    return 1


n, m = [int(x) for x in input().split()]
price = [int(x) for x in input().split()]
parent = [x for x in range(n + 1)]
conn = []
cost = 0
nodes = 0
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    if dsuUnion(a, b):
        nodes += 1
for i in range(2, n + 1):
    conn.append([abs(price[i - 1] - price[i - 2]), i - 1, i])
conn.sort()
for v, a, b in conn:
    if dsuUnion(a, b):
        cost += v
        nodes += 1
print(cost)
