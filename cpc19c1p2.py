import sys
from bisect import bisect_right
input = sys.stdin.readline


n, r = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
maxFit = 0
numbers.sort()
for i in range(n):
    ind = bisect_right(numbers, numbers[i] + r) - 1
    maxFit = max(maxFit, ind - i + 1)
print(maxFit)
