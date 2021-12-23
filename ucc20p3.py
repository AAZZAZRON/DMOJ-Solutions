from sys import stdin
from bisect import bisect_right
input = stdin.readline


bales = int(input())
num = int(input())
tractors = [int(x) for x in input().split()]
size = int(input())
farm = input()[:-1]
sizes = 0
current = 0
for i in farm:
    if i == "1":
        sizes = max(current, sizes)
        current = 0
    else:
        current += 1
index = bisect_right(tractors, sizes)
number = tractors[index - 1]

if bales % number == 0:
    print(bales // number)
else:
    print(bales // number + 1)
