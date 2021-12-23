sieve = [True] * 100001
sieve[0] = sieve[1] = False
psa = [0]
for i in range(1, 100001):
    if sieve[i]:
        psa.append(psa[-1] + i)
        for j in range(i + i, 100001, i):
            sieve[j] = False
    else:
        psa.append(psa[-1])
for _ in range(5):
    print(psa[int(input())])
