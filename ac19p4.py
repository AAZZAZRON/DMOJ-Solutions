from sys import stdin
input = stdin.readline


num = int(input())
points = {tuple([int(x) for x in input().split()]) for i in range(num)}
# print(points)
area = 0
for a, b in points:
    for c, d in points:
        if a == c and b == d:
            continue
        if (c, b) in points and (a, d) in points:
            area = max(area, (d - b) * (c - a))
print(area)
