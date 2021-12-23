def half(val):
    val //= 2
    if val % 2 == 1:
        return val
    return val - 1


def solve(num):
    for i in range(half(num), 1, -2):
        if sieve[i]:
            if sieve[num - i] and i <= num - i:
                return [i, num - i]
            elif i <= num // 3:
                for j in range(half(num - i), 1, -2):
                    if sieve[j] and sieve[num - i - j] and i <= j <= num - i - j:
                        return [i, j, num - i - j]


sieve = [True] * 10000001
sieve[0] = sieve[1] = False
for i in range(10000001):
    if sieve[i]:
        for j in range(i + i, 10000001, i):
            sieve[j] = False
for _ in range(5):
    num = int(input())
    if sieve[num]:
        numbers = [num]
    elif num % 2 == 0 and sieve[num // 2]:
        numbers = [num // 2, num // 2]
    elif num % 3 == 0 and sieve[num // 3]:
        numbers = [num // 3, num // 3, num // 3]
    else:
        # let i be the smallest number
        # let j be the second smallest number
        # let num - i - j be the largest number
        numbers = solve(num)
    print(f"{num} = {' + '.join([str(x) for x in numbers])}")
