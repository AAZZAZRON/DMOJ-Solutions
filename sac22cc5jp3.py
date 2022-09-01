import sys
input = sys.stdin.readline
n, q = [int(x) for x in input().split()]
media = [set() for _ in range(n + 1)]
for _ in range(q):
    a, b, name = input().split()
    a = int(a)
    b = int(b)
    if a == 1:
        print(1 if name in media[b] else 0)
    else:
        media[b].add(name)