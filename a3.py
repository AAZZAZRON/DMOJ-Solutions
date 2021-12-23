from sys import stdin
input = stdin.readline


cases = int(input())
for i in range(cases):
    num = int(input())
    if num % 10 > 2:
        num += 10 - (num % 10)
    else:
        num -= (num % 10)
    num += 2
    for j in range(num, 20001, 10):
        if (j * j * j) % 1000 == 888:
            print(j)
            break
