from datetime import date
from sys import stdin
input = stdin.readline


num = int(input())
for i in range(num):
    day = [int(x) for x in input().split()]
    day[0] = 2020 if day[0] % 4 == 0 else 2019
    now = date(day[0], day[1], day[2])
    past = date(day[0], 1, 1)
    print((now - past).days + 1)
