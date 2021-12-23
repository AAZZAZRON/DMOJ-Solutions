from sys import stdin
from bisect import bisect_left
input = stdin.readline


nEmpty, nNot = [int(x) for x in input().split()]
empty = [int(input()) for i in range(nEmpty)]
notEmpty = sorted([int(input()) for j in range(nNot)])
cHouse = 0
distance = 0
# print(empty, notEmpty)

for house in empty:
    index = bisect_left(notEmpty, house, 0, nNot)
    if index == 0:
        closest = abs(notEmpty[0] - house)
    elif index == nNot:
        closest = abs(notEmpty[-1] - house)
    else:
        closest = min(abs(notEmpty[index] - house), abs(notEmpty[index - 1] - house))
    # print(closest)
    if closest > distance:
        cHouse = house
        distance = closest
print(cHouse)
