from sys import stdin
from math import ceil
input = stdin.readline


places = int(input())
degrees = sorted([float(input().split()[1]) for i in range(places)])
maxD = 0
for i in range(places - 1):
    if degrees[i + 1] - degrees[i] > maxD:
        maxD = degrees[i + 1] - degrees[i]
minDegrees = min(degrees[-1] - degrees[0], 360 - maxD)

print(ceil(minDegrees * 12))
