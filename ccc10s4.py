import sys
input = sys.stdin.readline


n = int(input())
costs = [[0] * 1002 for _ in range(1002)]  # cost from i to j (pens)
openings = [set() for _ in range(n + 1)]  # edges from pen i
openExits = [696969] * (n + 1)  # minimum value to exit the pen to the outside
conn = []  # connections for mst
for q in range(1, n + 1):
    m, *line = [int(x) for x in input().split()]
    nodes = line[:m]
    c = line[m:]
    for i in range(m):
        assert nodes[i] != 0
        assert c[i] >= 0
        ind = tuple(sorted([nodes[i], nodes[(i + 1) % m]]))
        openings[q].add(ind)
        for j in range(1, q):
            if ind in openings[j]:  # if ind in openings[j], means it is an inside connection
                openings[q].remove(ind)
                openings[j].remove(ind)
                conn.append([costs[ind[0]][ind[1]], q, j])
        costs[nodes[i]][nodes[(i + 1) % m]] = c[i]  # add cost
        costs[nodes[(i + 1) % m]][nodes[i]] = c[i]

for i in range(1, n + 1):  # for each pen
    for a, b in openings[i]:  # find the minimum cost to get to the outside
        assert costs[a][b] != 0
        openExits[i] = min(openExits[i], costs[a][b])
    conn.append([openExits[i], i, 0])

conn.sort()

inside = 0  # find mst with no outside
values = [{i} for i in range(n + 1)]
for c, a, b in conn:
    if b == 0:
        continue
    indA, indB = 0, 0
    for i in range(n, -1, -1):
        if a in values[i]:
            indA = i
        if b in values[i]:
            indB = i
    if indA != indB:
        values[min(indA, indB)] = values[min(indA, indB)].union(values[max(indA, indB)])
        values[max(indA, indB)] = set()
        inside += c

ct = 0
for i in values[1:]:  # check how many cycles there are
    if i != set():
        ct += 1

outside = 0  # solve for mst with outside
values = [{i} for i in range(n + 1)]
for c, a, b in conn:
    indA, indB = 0, 0
    for i in range(n, -1, -1):
        if a in values[i]:
            indA = i
        if b in values[i]:
            indB = i
    if indA != indB:
        values[min(indA, indB)] = values[min(indA, indB)].union(values[max(indA, indB)])
        values[max(indA, indB)] = set()
        outside += c

# print accordingly
if ct == 1:
    print(min(inside, outside))
else:
    print(outside)
