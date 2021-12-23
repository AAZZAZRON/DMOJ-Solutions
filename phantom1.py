import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


primes = []
sieve = [1] * 501
sieve[0] = sieve[1] = 0
for i in range(2, 501):
    if sieve[i]:
        primes.append(i)
        for j in range(i + i, 501, i):
            sieve[j] = 0


n = int(input())
for _ in range(n):
    start, end = [int(x) for x in input().split()]
    one = bisect_left(primes, start)
    two = bisect_right(primes, end - 1)
    print(two - one)
