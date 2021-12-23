import sys
input = sys.stdin.readline


numPoints = int(input())
points = []
x, y = [], []
for i in range(numPoints):
    coord = [int(x) for x in input().split(",")]
    x.append(coord[0])
    y.append(coord[1])
x.sort()
y.sort()
print(f"{x[0] - 1},{y[0] - 1}")
print(f"{x[-1] + 1},{y[-1] + 1}")
