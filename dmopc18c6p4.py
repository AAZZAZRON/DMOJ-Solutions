import sys
from bisect import bisect_right
input = sys.stdin.readline


num, nP, nM = [int(x) for x in input().split()]
tanks = [[int(x) for x in input().split()] + [q + 1] for q in range(num)]
physical = sorted([int(x) for x in input().split()])
magical = sorted([int(x) for x in input().split()])
minimum, index = 69696969696969696969696969, 0
physicalPSA = [0]
magicalPSA = [0]
[physicalPSA.append(physicalPSA[-1] + x) for x in physical]
[magicalPSA.append(magicalPSA[-1] + x) for x in magical]
for defense, resistance, ind in tanks:
    current = 0
    pInd = bisect_right(physical, defense)
    mInd = bisect_right(magical, resistance)
    current += physicalPSA[-1] - physicalPSA[pInd]
    current -= defense * (nP - pInd)
    current += magicalPSA[-1] - magicalPSA[mInd]
    current -= resistance * (nM - mInd)
    if current < minimum:
        minimum = current
        index = ind
print(index)
