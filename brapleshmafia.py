import sys
input = sys.stdin.readline


n, k = [int(x) for x in input().split()]
counter = 0
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    counter += a * b
    counter %= k
print(counter)
