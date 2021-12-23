import sys
input = sys.stdin.readline

sieve = [1] * 2000000
sieve[0] = sieve[1] = 0
for i in range(2000000):
    if sieve[i]:
        for j in range(i + i, 2000000, i):
            sieve[j] = 0


for _ in range(int(input())):
    x = int(input()) * 2
    for i in range(1000000):
        if sieve[i] and sieve[x - i]:
            print(i, x - i)
            break
