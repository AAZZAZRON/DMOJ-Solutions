sieve = [1] * 10001
sieve[0] = sieve[1] = 0
for i in range(10001):
    if sieve[i]:
        for j in range(i + i, 10001, i):
            sieve[j] = 0
for _ in range(5):
    nums = [x for x in range(1, int(input()) + 1)]
    numbers = [0] * 10001
    values = set()
    for num in nums:
        while num != 1:
            for i in range(10001):
                if sieve[i] and num % i == 0:
                    num //= i
                    numbers[i] += 1
                    values.add(i)
                    break
    arr = []
    for i in sorted(list(values)):
        arr.append(f"{i}^{numbers[i]}")
    print(" * ".join(arr))
