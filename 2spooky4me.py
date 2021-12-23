import sys
input = sys.stdin.readline


lines, houses, spooky = [int(x) for x in input().split()]
points = [(houses + 1, 0)]
for i in range(lines):
    start, end, add = [int(x) for x in input().split()]
    points.append((start, add))
    points.append((end + 1, -add))
points.sort()
current = 0
for i in range(len(points) - 1):
    current += points[i][1]
    if current >= spooky:
        houses -= (points[i + 1][0] - points[i][0])
print(houses)
