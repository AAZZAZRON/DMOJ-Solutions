from sys import stdin, exit
input = stdin.readline


num, length, uses, change = [int(x) for x in input().split()]
alpacas = [int(input()) for _ in range(num)]
mySpeed = int(input())

for speed in alpacas:
    while mySpeed <= speed:
        if uses == 0:
            print("NO")
            exit()
        speed = speed * (100 - change) // 100
        uses -= 1
        if speed == 0:
            break
print("YES")
