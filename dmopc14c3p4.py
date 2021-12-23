from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline


factors = [2] * 100001
factors[0] = 0
factors[1] = 1
factorList = [[] for _ in range(100001)]
for i in range(2, 100001):
    for j in range(i + i, 100001, i):
        factors[j] += 1
for i in range(100001):
    factorList[factors[i]].append(i)
# print(factors)
t = int(input())
for _ in range(t):
    num, start, end = [int(x) for x in input().split()]
    startInd = bisect_left(factorList[num], start)
    endInd = bisect_right(factorList[num], end)
    print(endInd - startInd)
