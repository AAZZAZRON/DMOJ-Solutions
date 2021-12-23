sieve = [1] * 1000
sieve[0] = sieve[1] = 0
primes = []
for i in range(2, 1000):
    if sieve[i]:
        primes.append(i)
        for j in range(i, 1000, i):
            sieve[j] = 0
for _ in range(5):
    n = int(input())
    c = 0
    for i in primes:
        if n % i == 0:
            n //= i
            c += 1
    if c == 3:
        print("valid")
    else:
        print("not")
