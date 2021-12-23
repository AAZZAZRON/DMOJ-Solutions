from sys import stdin
input = stdin.readline


def isNasty(number):
    factors = set()
    for j in range(1, int(number ** 1/2)):
        if number % j == 0:
            factor = j + (number // j)
            if factor in factors:
                return True
            second = abs(j - (number // j))
            factors.add(second)
    return False


num = int(input())
for i in range(num):
    new = int(input())
    if isNasty(new):
        print(f"{new} is nasty")
    else:
        print(f"{new} is not nasty")
