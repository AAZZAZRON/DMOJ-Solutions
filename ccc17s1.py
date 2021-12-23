import sys
input = sys.stdin.readline


n = int(input())
one = [int(x) for x in input().split()]
two = [int(x) for x in input().split()]
a, b = 0, 0
day = 0
for i in range(n):
    a += one[i]
    b += two[i]
    if a == b:
        day = i + 1
print(day)
