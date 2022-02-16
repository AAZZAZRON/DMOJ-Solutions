import sys
input = sys.stdin.readline

sieve = [1] * 1000001
setprimes = set()
primes = []
sieve[0] = sieve[1] = 0
for i in range(2, 1000001):
    if sieve[i]:
        primes.append(i)
        setprimes.add(i)
        for j in range(i, 1000001, i):
            sieve[j] = 0


for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    elif n == 3:
        print(-1)
    elif n == 4:
        print(3, 1, 4, 2)
    elif n == 5:
        print(3, 1, 4, 2, 5)
    elif n == 6:
        print(1, 3, 5, 2, 4, 6)
    elif n == 7:
        print(2, 4, 6, 1, 3, 5, 7)
    else:
        if n % 2 == 1:
            odd = 1
            n -= 1
        else:
            odd = 0
        p, q = 0, 0
        for i in primes:
            if n - i in setprimes:
                p = i
                q = n - i
                break
        assert p != 0 and q != 0
        arr = [0] * (n + 1)
        for i in range(1, n + 1):
            if arr[i - 1] + p > n:
                arr[i] = arr[i - 1] - q
            else:
                arr[i] = arr[i - 1] + p
        if odd:
            ind = arr.index(n + 1 - p)
            print(" ".join([str(x) for x in arr[ind + 1:]]), " ".join([str(x) for x in arr[1:ind + 1]]), n + 1)
        else:
            print(" ".join([str(x) for x in arr[1:]]))
