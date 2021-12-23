import sys
input = sys.stdin.readline


n = int(input())
sweep = [0] * 10000000
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    sweep[a] += 1
    sweep[b] -= 1
maximum = 0
counter = 0
for i in sweep:
    counter += i
    maximum = max(maximum, counter)
print(maximum)
