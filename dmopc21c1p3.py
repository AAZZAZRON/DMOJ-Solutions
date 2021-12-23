import sys
input = sys.stdin.readline


def ask(l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    ask(l, mid)
    ask(mid + 1, r)
    print("?", mid - l + 1, r - mid)
    sys.stdout.flush()
    print(" ".join([str(x) for x in range(l, mid + 1)]))
    sys.stdout.flush()
    print(" ".join([str(x) for x in range(mid + 1, r + 1)]))
    sys.stdout.flush()
    ct, *arr = [int(x) - 1 for x in input().split()]
    for i in arr:
        vis[i] = 1
    return


n, m = [int(x) for x in input().split()]
edges = [[int(x) for x in input().split()] for i in range(m)]
vis = [0] * m
ask(1, n)
p = [0] * m
for i in range(m):
    if not vis[i]:
        p[i] = 1
print("!", "".join([str(x) for x in p]))
