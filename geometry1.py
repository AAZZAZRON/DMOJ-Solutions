import sys
from math import sqrt
input = sys.stdin.readline


numTriangles = int(input())
for i in range(numTriangles):
    numbers = [int(x) for x in input().split()]
    x = [numbers[0], numbers[2], numbers[4]]
    y = [numbers[1], numbers[3], numbers[5]]

    one = (numbers[0], numbers[1])
    two = (numbers[2], numbers[3])
    three = (numbers[4], numbers[5])
    area = abs((0.5 * ((one[0] - two[0]) * (one[1] - three[1]) - (one[0] - three[0]) * (one[1] - two[1]))))
    area = str(area)
    sideOne = sqrt((two[0] - one[0]) ** 2 + (two[1] - one[1]) ** 2)
    sideTwo = sqrt((three[0] - two[0]) ** 2 + (three[1] - two[1]) ** 2)
    sideThree = sqrt((one[0] - three[0]) ** 2 + (one[1] - three[1]) ** 2)
    prim = round((sideOne + sideTwo + sideThree) * 100) / 100
    prim = str(prim)
    print(area + "0" * (4 - (len(area) - area.index(".") + 1)), prim + "0" * (4 - (len(prim) - prim.index(".") + 1)))
