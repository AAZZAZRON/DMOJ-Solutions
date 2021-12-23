from math import sqrt
# based on editorial


def solve(n):
    if n == 1:
        return 1
    elif n in memo:
        return memo[n]
    tmp = 0
    for i in range(1, int(sqrt(n)) + 1):
        tmp += solve(i) * (n // i - n // (i + 1))
        if i >= 2 and n // i > int(sqrt(n)):
            tmp += solve(n // i)
    memo[n] = tmp
    return tmp


n = int(input())
memo = {}
print(solve(n))
# print(memo)
