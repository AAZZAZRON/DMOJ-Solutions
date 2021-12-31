import sys
input = sys.stdin.readline


n, m, s, f, l, r = [int(x) for x in input().split()]
throw = [int(x) for x in input().split()]
kM = 0
for i in range(m):
    if throw[i] == f:
        kM = i + 1
p = [[0] * m for _ in range(n)]
total = 0
if f != s and f not in throw:
    print(-1)
    sys.exit()
if r == 0:
    if f != s:
        print(-1)
    else:
        print(total)
        [print(" ".join([str(x) for x in y])) for y in p]
    sys.exit()
if kM != 0:
    total += 1
    p[s - 1][kM - 1] = 1
    for i in range(1, n + 1):
        if total >= l or i == s:
            continue
        p[i - 1][kM - 1] = 1
        total += 1
for i in range(1, n + 1):
    for j in range(1, kM):
        if total >= l:
            continue
        assert p[i - 1][j - 1] == 0
        p[i - 1][j - 1] = 1
        total += 1
for i in range(1, n + 1):
    if i == f:
        continue
    for j in range(kM + 1, m + 1):
        if total >= l:
            continue
        assert p[i - 1][j - 1] == 0
        p[i - 1][j - 1] = 1
        total += 1
if total < l or total > r:
    print(-1)
else:
    s = 0
    for i in p:
        s += i.count(1)
    assert s == total
    print(total)
    [print(" ".join([str(x) for x in y])) for y in p]
