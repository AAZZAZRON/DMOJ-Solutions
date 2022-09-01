from math import sqrt
n = int(input())
fact = 1
for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        fact = n // i
        break

print(n - fact)
