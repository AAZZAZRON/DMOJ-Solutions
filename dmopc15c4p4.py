import sys
from bisect import bisect_left
input = sys.stdin.readline


n, k, q = [int(x) for x in input().split()]
sequence = [int(x) for x in input().split()]
psa = [0]
indexes = {}
for i in range(n):
    x = sequence[i]
    psa.append(psa[-1] + x)
    if x in indexes:
        indexes[x].append(i + 1)
    else:
        indexes[x] = [i + 1]
for _ in range(q):
    a, b, x, y = [int(r) for r in input().split()]
    if a in indexes.keys():
        one = bisect_left(indexes[a], x)
        two = bisect_left(indexes[a], y + 1)
        hasA = one != two
    else:
        hasA = False
    if b in indexes.keys():
        one = bisect_left(indexes[b], x)
        two = bisect_left(indexes[b], y + 1)
        hasB = one != two
    else:
        hasB = False
    if psa[y] - psa[x - 1] > k and hasA and hasB:
        print("Yes")
    else:
        print("No")
