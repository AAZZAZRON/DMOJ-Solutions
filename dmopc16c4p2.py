import sys
from bisect import bisect_left
input = sys.stdin.readline

points = []
batches = []
failed = []
total = 0
n = int(input())
for _ in range(n):
    a, b, c = [int(x) for x in input().split()]
    batches.append([a, b])
    points.append(c)
for _ in range(int(input())):
    failed.append(int(input()))
failed.sort()
for i in range(n):
    a, b = batches[i]
    if bisect_left(failed, a) == bisect_left(failed, b + 1):
        total += points[i]
print(total)
