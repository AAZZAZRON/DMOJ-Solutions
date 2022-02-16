import sys
from bisect import bisect_left
input = sys.stdin.readline


length, num = [int(x) for x in input().split()]
maximum = 0
paint = [[int(x) for x in input().split()] for _ in range(num)]

paint.sort()
ins = [[] for _ in range(num + 1)]
m = 0
for i in range(num):
    a, b = paint[i]
    for x in ins[i]:
        m = max(m, x)
    opt = m + b - a + 1
    maximum = max(maximum, opt)
    ins[bisect_left(paint, [b, 0])].append(opt)
print(length - maximum)
