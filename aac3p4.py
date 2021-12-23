import sys
input = sys.stdin.readline


n, m = [int(x) for x in input().split()]
rows, col = {}, {}
c = 0
for i in [int(x) for x in input().split()]:
    c += 1
    if i == -1:
        continue
    if i - c in rows:
        rows[i - c] += 1
    else:
        rows[i - c] = 1
c = 0
for i in [int(x) for x in input().split()]:
    c += 1
    if i == -1:
        continue
    if i - c in col:
        col[i - c] += 1
    else:
        col[i - c] = 1
# print(rows)
# print(col)
final = 0
for i in rows:
    if i in col:
        final += min(rows[i], col[i])
print(final)
