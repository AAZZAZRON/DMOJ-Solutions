from sys import stdin
from math import sqrt, floor
input = stdin.readline


num, p = [int(x) for x in input().split()]
maxName, maxVal, minName, minVal = "", 0, "", 999999999999
for _ in range(num):
    name, math, cs, eng = input().split()
    math = 4.0 * sqrt(int(math))
    cs = 3.0 * (int(cs) ** p)
    eng = 4.0 * int(eng)
    val = floor(math + cs - eng)
    if val > maxVal:
        maxVal = val
        maxName = name
    if val < minVal:
        minVal = val
        minName = name
print(maxName, maxVal)
print(minName, minVal)
