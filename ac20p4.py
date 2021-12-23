import sys
input = sys.stdin.readline


n, q = [int(x) for x in input().split()]
connections = [set() for _ in range(n + 1)]
pairs = set()
for _ in range(q):
    a, b = [int(x) for x in input().split()]
    connections[min(a, b)].add(max(a, b))
    pairs.add((min(a, b), max(a, b)))
# print(connections)
found3 = [3001, 3001, 3001]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if j in connections[i]:
            tmp = connections[j].intersection(connections[i])
            if tmp != set():
                found3 = min(found3, sorted([i, j, min(tmp)]))
if found3[0] != 3001:
    print(3)
    print(" ".join([str(x) for x in found3]))
    sys.exit()
found4 = [3001, 3001, 3001, 3001]
for a, b in pairs:
    for c, d in pairs:
        if a != c and a != d and b != c and b != d and a != b and c != d:
            found4 = min(found4, sorted([a, b, c, d]))
if found4[0] != 3001:
    print(4)
    print(" ".join([str(x) for x in found4]))
    sys.exit()
print(-1)
