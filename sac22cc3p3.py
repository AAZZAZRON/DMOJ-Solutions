import math

n = int(input())
arr = [int(x) for x in input().split()]
for i in range(1, math.floor(math.log10(max(arr)) + 1) + 1):
    t = []
    for j in arr:
        t.append([j % (10 ** i), j])
    t.sort()
    arr = [x[1] for x in t]
    print(*arr)

