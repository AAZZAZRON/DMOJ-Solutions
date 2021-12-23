start, end = int(input()), int(input())
sieve = [1] * (end + 1)
sieve[0] = sieve[1] = 0
for i in range(end + 1):
    if sieve[i] == 1:
        for j in range(i + i, end + 1, i):
            sieve[j] += 1
for i in range(start, end + 1):
    print(sieve[i]) if sieve[i] == 1 else print(sieve[i] - 1)
