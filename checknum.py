import sys
import math
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    low, high = 1, n
    while high - low > 1:
        mid = (low + high) // 2
        if mid * mid <= n:
            low = mid
        else:
            high = mid
    v = low
    nO = math.ceil(v / 9)
    nE = math.ceil((n - v * v) / 9)
    if nO > nE:
        print(nO * 2 - 1)
    else:
        print(nE * 2)
