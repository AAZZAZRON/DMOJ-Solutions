candies, multiple = [int(x) for x in input().split()]
primes = [True for i in range(candies + 1)]
primes[0] = False
primes[1] = False
combos = 0
for p in range(2, candies + 1):
    if primes[p]:
        combos += (candies - p) // multiple + 1
        combos += (candies - p - 1) // multiple + 1

        for i in range(p * 2, candies + 1, p):
            primes[i] = False
# print(primes)
print(combos)
