from sys import stdin
input = stdin.readline


num = int(input())
for i in range(num):
    year, month, day = [int(x) for x in input().split()]
    if year < 1989:
        print("Yes")
    elif year == 1989 and month < 2:
        print("Yes")
    elif year == 1989 and month == 2 and day <= 27:
        print("Yes")
    else:
        print("No")
