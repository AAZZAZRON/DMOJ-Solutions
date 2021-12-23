from sys import stdin
input = stdin.readline


length = int(input())
start, end = [int(x) for x in input().split()]
counter = 0
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    counter += max(-1, min(end, b) - max(start, a)) + 1
print(counter)
