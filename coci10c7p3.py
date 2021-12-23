from bisect import bisect_left


values = [[] for _ in range(7)]
n, p = [int(x) for x in input().split()]
c = 0
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    values[a].append(b)

for line in values[1:]:
    arr = []
    length = 0
    for i in line:
        ind = bisect_left(arr, i + 1)
        c += length - ind
        length = ind
        arr = arr[:ind]
        if (length != 0 and arr[-1] != i) or length == 0:
            length += 1
            c += 1
            arr.append(i)
print(c)
