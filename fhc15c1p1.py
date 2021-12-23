from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline


N = 10000001 # get the sieves
isPrime = [True] * N
isPrime[0] = isPrime[1] = False
amounts = [0] * N
primeAmounts = [[] for _ in range(10000)]
for i in range(2, N):
    if isPrime[i]:
        for j in range(i, N, i):
            isPrime[j] = False
            amounts[j] += 1
for i in range(2, N):
    primeAmounts[amounts[i]].append(i)
num = int(input())
for q in range(1, num + 1):
    start, end, factors = [int(x) for x in input().split()]
    x = bisect_left(primeAmounts[factors], start)
    y = bisect_right(primeAmounts[factors], end)
    number = y - x
    print(f"Case #{q}: {number}")
