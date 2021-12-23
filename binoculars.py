import sys
input = sys.stdin.readline

n, q = [int(x) for x in input().split()]
current = [0] * (n + 1)
added = [0] * (n + 1)
for _ in range(q):
    a, b, c = [int(x) for x in input().split()]
    added[a] += max(0, -(current[a] - c))
    current[a] = max(0, current[a] - c)
    current[b] += c
print(sum(added))
print(" ".join([str(x) for x in added[1:]]))