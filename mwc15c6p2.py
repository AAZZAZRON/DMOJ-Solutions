sieve = [True] * 100001
sieve[0] = False
sieve[1] = False
before = [0] * 100001
last = "no can do"

# sieve all primes
for i in range(100001):
    before[i] = last
    if sieve[i]:
        for j in range(i, 100001, i):
            sieve[j] = False
        last = i

n = int(input())
for x in [int(x) for x in input().split()]:
    print(before[x])
