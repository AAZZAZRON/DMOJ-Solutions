import sys
from bisect import bisect_left
input = sys.stdin.readline


def update(ind, v):
    while ind <= 4000000:
        BIT[ind] = max(BIT[ind], v)
        ind += ind & (-ind)


def query(ind):
    m = 0
    while ind >= 1:
        m = max(m, BIT[ind])
        ind -= ind & (-ind)
    return m


n = int(input())
BIT = [0] * 4000001
tmp = []
v = set()
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    tmp.append([a, b, a - b, a + b])
    v.add(a)
    v.add(b)
    v.add(a - b)
    v.add(a + b)
v = sorted(list(v))
m = {}
for i in range(len(v)):
    m[v[i]] = i + 1
tmp.sort()
alpacas = [[m[x] for x in tmp[i]] for i in range(n)]
dp = [1] * n
ins = [[] for _ in range(n + 1)]
for i in range(n):
    a, b, c, d = alpacas[i]
    for x, y in ins[i]:
        update(x, y)
    dp[i] = query(c) + 1
    ind = bisect_left(alpacas, [d, -1, 0, 0])
    ins[ind].append([a, dp[i]])
# print(alpacas)
# print(dp)
# print(BIT[:30])
print(max(dp))
