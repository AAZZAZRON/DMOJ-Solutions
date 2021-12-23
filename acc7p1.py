from sys import stdin
input = stdin.readline


for _ in range(int(input())):
    x = int(input())
    print(x - 1) if x != 2 else print(2)
