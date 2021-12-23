import sys
from math import floor
input = sys.stdin.readline


def calc(i, j):
    y = (i - j) // 2
    x = j + y
    c = 0
    for a, b in kings:
        c += max(abs(x - a), abs(y - b))
    return c


n = int(input())
aX, aY = [], []
kings = []
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    aX.append(a + b)
    aY.append(a - b)
    kings.append([a, b])
aX.sort()
aY.sort()
if n % 2 == 0:
    one = floor((aX[n // 2 - 1] + aX[n // 2]) / 2)
    two = floor((aY[n // 2 - 1] + aY[n // 2]) / 2)
else:
    one, two = aX[n // 2], aY[n // 2]
print(min(calc(one, two), calc(one + 1, two), calc(one, two + 1), calc(one + 1, two + 1)))
