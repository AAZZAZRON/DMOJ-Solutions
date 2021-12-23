from bisect import bisect_left, bisect_right


sieve = [True] * 1000000
sieve[0] = sieve[1] = False
palindromePrimes = []
for i in range(1000000):
    if sieve[i]:
        if str(i) == str(i)[::-1]:
            palindromePrimes.append(i)
        for j in range(i + i, 1000000, i):
            sieve[j] = False
for _ in range(5):
    start, end = [int(x) for x in input().split()]
    a = bisect_left(palindromePrimes, start)
    b = bisect_right(palindromePrimes, end + 1)
    print(b - a)
