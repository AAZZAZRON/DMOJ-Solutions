from sys import stdin
input = stdin.readline


num = int(input())
slope = {}
point = {}
points = []
for _ in range(num):
    x, y = [int(x) for x in input().split()]
    if x in slope:
        slope[x] += 1
    else:
        slope[x] = 1
    if (x, y) in point:
        point[(x, y)] += 1
    else:
        point[(x, y)] = 1
    points.append([x, y])

counter = 0
for x, y in points:
    counter += num - slope[x] # remove all same slopes
    counter += point[(x, y)] - 1
print(counter // 2)
