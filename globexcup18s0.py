import sys
input = sys.stdin.readline


def calculate(pos, arr):
    c = 0
    for p in arr:
        c += abs(p - pos)
    return c


n = int(input())
aX, aY = [], []
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    aX.append(a)
    aY.append(b)
aX.sort()
aY.sort()
tX, tY = 0, 0
if n % 2 == 0:
    v = aX[n // 2 - 1] + aX[n // 2]
    v /= 2
    tX = max(calculate(int(v), aX), calculate(int(v + 0.5), aX))
    v = aY[n // 2 - 1] + aY[n // 2]
    v /= 2
    tY = max(calculate(int(v), aY), calculate(int(v + 0.5), aY))
else:
    tX = calculate(aX[n // 2], aX)
    tY = calculate(aY[n // 2], aY)
print(tX + tY)
