import sys
input = sys.stdin.readline


numChairs, roomSize = [int(x) for x in input().split()]
xH, xL, yH, yL = 0, 0, 0, 0
for i in range(numChairs):
    a, b = [int(x) for x in input().split()]
    xL += a - 1
    xH += roomSize - a
    yL += b - 1
    yH += roomSize - b
money = 0
if xL > xH:
    money += xL
else:
    money += xH
if yL > yH:
    money += yL
else:
    money += yH
print(money)
