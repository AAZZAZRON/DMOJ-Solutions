from math import ceil
from sys import stdin
input = stdin.readline


num = int(input())
for i in range(num):
    nQ, w, l, want = [int(x) for x in input().split()]
    start = nQ * l
    increment = w + l
    moves = ceil((want + start) / increment)
    if moves > nQ:
        print(-1)
    else:
        print(moves)
