from sys import stdin
from bisect import bisect_left
from math import sqrt
input = stdin.readline


num, q = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
positions = [[99999999] for _ in range(100001)]
for i in range(num):
    positions[numbers[i]].append(i)
numbers = set(numbers)
for _ in range(q):
    a, b, num = [int(x) for x in input().split()]
    a -= 1
    found = False
    for i in range(1, int(sqrt(num)) + 2):
        if num % i == 0:
            j = num // i
            if i == j:
                continue

            if bisect_left(positions[i], a) == bisect_left(positions[i], b):
                continue
            if bisect_left(positions[j], a) == bisect_left(positions[j], b):
                continue
            found = True
            break
    if found:
        print("YES")
    else:
        print("NO")
