import sys
input = sys.stdin.readline


n, v = [int(x) for x in input().split()]
items = [input().split() for _ in range(n)]
final = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if int(items[i][1]) + int(items[j][1]) + \
                int(items[k][1]) <= v:
                final.append(" ".join(sorted([items[i][0], items[j][0], items[k][0]])))

[print(x) for x in sorted(final)]