from sys import stdin
input = stdin.readline


lines = int(input())
for i in range(lines):
    a, b, c = sorted(int(x) for x in input().split())
    value = a ** 2 + b ** 2
    result = c ** 2
    if value < result:
        print("O")
    elif value == result:
        print("R")
    elif value > result:
        print("A")
