from math import sqrt
a, b = [int(x) for x in input().split()]
for i in range(1, int(sqrt(a)) + 1):
    if a % i == 0:
        if b % i == 0:
            print(i, a // i, b // i)
        if a // i != i and a % (a // i) == 0 and b % (a // i) == 0:
            print(a // i, i, b // (a // i))
