from sys import stdin
input = stdin.readline

num = int(input())
minimum = 9999999999
for _ in range(num):
    numbers, *summation = [int(x) for x in input().split()]
    minimum = min(sum(summation), minimum)
print(minimum)
