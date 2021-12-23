num, k = [int(x) for x in input().split()]
sieve = [True] * (num + 1)
sieve[0] = sieve[1] = False
primes = []
for i in range(num + 1):
    if sieve[i]:
        primes.append(i)
        for j in range(i + i, num + 1, i):
            sieve[j] = False
dp = [999999] * (num + 1)
counter = 0
dp[0] = 0
for i in range(num + 1):
    if dp[i] == 999999:
        continue
    for j in primes:
        if i + j < num + 1:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
        else:
            break
for i in dp:
    if i == k:
        counter += 1
print(counter)
