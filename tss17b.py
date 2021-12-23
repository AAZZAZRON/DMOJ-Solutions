import sys
from bisect import bisect_right


x = sys.stdin.readline().split()
numHouses = int(x[0])
numScenarios = int(x[1])
houses = []
for i in range(0, numHouses):
    x = sys.stdin.readline().split()
    houses.append((int(x[0]) ** 2 + int(x[1]) ** 2) ** 0.5)
houses.sort()
for i in range(0, numScenarios):
    radius = int(sys.stdin.readline())
    low = bisect_right(houses, radius)
    print(low)
