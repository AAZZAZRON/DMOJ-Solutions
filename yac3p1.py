import sys
input = sys.stdin.readline
n, m, a, b = [int(x) for x in input().split()]
first = -1
v = []
for i in range(m):
    arr = [int(x) for x in input().split()]
    if arr[0] == -1 and first == -1:
        first = i
    if arr[0] == -1:
        v.append([1, 2])
    else:
        v.append(arr)
for i in range(m - 1, first, -1):
    if v[i][0] == b:
        b = v[i][1]
    elif v[i][1] == b:
        b = v[i][0]
for i in range(first):
    if v[i][0] == a:
        a = v[i][1]
    elif v[i][1] == a:
        a = v[i][0]
if a == b:
    v[first] = [a - 1 if a - 1 >= 1 else n, a + 1 if a + 1 <= n else 1]
else:
    v[first] = [a, b]
[print(*x) for x in v]
