import sys
input = sys.stdin.readline


def calculate(pos):
    c = 0
    for p, w, d in people:
        walk = abs(pos - p) - d
        c += max(0, walk) * w
    return c


n = int(input())
people = [[int(x) for x in input().split()] for _ in range(n)]
time = min(calculate(0), calculate(1000000000))
low, high = 0, 1000000000
while high - low > 1:
    mid = (low + high) // 2
    v = calculate(mid)
    v2 = calculate(mid + 1)
    time = min(time, v, v2)
    if v < v2:
        high = mid
    else:
        low = mid
print(time)
