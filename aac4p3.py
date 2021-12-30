from collections import defaultdict


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


n, m = [int(x) for x in input().split()]
points = [[int(x) for x in input().split()] for _ in range(n)]
ct = 0
used = set()
for _ in range(m):
    freq = defaultdict(int)
    k, d = [int(x) for x in input().split()]
    g = gcd(k, d)
    if (k // g, d // g) in used:
        continue
    used.add((k // g, d // g))
    for a, b in points:
        ans = d * b - k * a
        ct += freq[ans]
        freq[ans] += 1
print(ct)
