def dfs(node):
    v = conn[node]
    m = 0
    for i in v:
        assert len(i) == 2
        m = max(m, dfs(i[0]) + i[1])
    return m


n, r = [int(x) for x in input().split()]
conn = [[] for _ in range(2 ** (n + 1))]
for _ in range(2 ** n - 1):
    a, b, c, change = [int(x) for x in input().split()]
    conn[a].append([b, change])
    conn[a].append([c, 0])
print(r + dfs(1))
