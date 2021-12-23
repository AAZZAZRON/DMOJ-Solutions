import sys
from bisect import bisect_left
input = sys.stdin.readline


sieve = [1] * 1000000
primes = []
sieve[0] = sieve[1] = 1
for i in range(2, 1000000):
    if sieve[i]:
        sieve[i] = i
        primes.append(i)
        for j in range(i + i, 1000000, i):
            sieve[j] = 0
    sieve[i] += sieve[i - 1]
q = int(input())
for _ in range(q):
    start, func = [int(x) for x in input().split()]
    end = primes[bisect_left(primes, start) + func - 1]
    print(end, sieve[end] - sieve[start - 1])
