import sys
input = sys.stdin.readline


n = int(input())
numbers = set([int(x) for x in input().split()])
maximum = 0
for a in numbers:
    for b in numbers:
        if a == b:
            continue
        if a < b and b + (b - a) in numbers:
            maximum = max(maximum, a + b + (b + (b - a)))
print(maximum)
