from sys import stdin
input = stdin.readline


rows, col, k = [int(x) for x in input().split()]
r, c = set(), set()

for _ in range(k):
    a, b = [int(x) for x in input().split()]
    if a in r:
        r.remove(a)
    else:
        r.add(a)
    if b in c:
        c.remove(b)
    else:
        c.add(b)
maximum = max(len(c), len(r))
cL, rL = len(c), len(r)
print(maximum)
c = list(c)
r = list(r)
for i in range(maximum):
    if i >= rL:
        print(1, c[i])
    elif i >= cL:
        print(r[i], 1)
    else:
        print(r[i], c[i])
