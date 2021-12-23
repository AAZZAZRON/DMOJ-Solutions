import sys
from math import sqrt
input = sys.stdin.readline


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


num = int(input())
numbers = [int(x) for x in input().split()]
a = numbers[0]
for remainder in numbers[1:]:
    if a < remainder:
        a, remainder = remainder, a
    while remainder != 0:
        b = remainder
        remainder = a % b
        a = b
maximum = 1
for i in range(int(sqrt(a)), 0, -1):
    if a % i == 0:
        if isPrime(a // i):
            maximum = max(maximum, a // i)
        elif isPrime(i):
            maximum = max(maximum, i)
print(maximum) if maximum != 1 else print("DNE")
