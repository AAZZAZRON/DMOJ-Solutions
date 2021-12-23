import sys
input = sys.stdin.readline


money = int(input())
items = int(input())
prices = [int(input()) for _ in range(items)]

sieve = [1] * (money + 1)
sieve[0] = sieve[1] = 0
primes = []
for i in range(2, money + 1):
    if sieve[i]:
        if i <= money:
            primes.append(i)
        for j in range(i + i, money + 1, i):
            sieve[j] = 0
dp = [0] * (money + 1)
dp[0] = 1
# let dp[i] represent the amount of each object
# that Bob buys with i dollars
for k in range(items):
    primeTime = 0
    price = prices[k]
    for i in range(money, -1, -1):
        if dp[i]:
            for p in primes:
                if i + p * price > money:
                    break
                dp[i + p * price] = 1
        dp[i] = 0

# print(dp)
if 1 in dp:
    print("its primetime")
    sys.exit()
print("not primetime")
