import sys
sys.setrecursionlimit(200000)

'''
noBehind
oneBehind
twoBehind
someBehind
'''


def noBehind(n):
    if n == 1:
        return 1
    if n <= 0:
        return 0
    if memoNo[n]:
        return memoNo[n]
    memoNo[n] = (noBehind(n - 1) + oneBehind(n - 2) + twoBehind(n - 3)) % MOD
    return memoNo[n]


def oneBehind(n):
    if n <= 0:
        return 0
    if memoOne[n]:
        return memoOne[n]
    ct = 0
    ct += noBehind(n - 1) + oneBehind(n - 2)
    ct += noBehind(n - 2)
    ct += noBehind(n - 3) + oneBehind(n - 4)
    ct += someBehind(n - 3)
    ct %= MOD
    memoOne[n] = ct
    return memoOne[n]


def twoBehind(n):
    if n <= 0:
        return 0
    if memoTwo[n]:
        return memoTwo[n]
    ct = 0
    ct += noBehind(n - 2)
    ct += someBehind(n)
    memoTwo[n] = ct % MOD
    return memoTwo[n]


def someBehind(n):
    if n <= 0:
        return 0
    if memoSome[n]:
        return memoSome[n]
    ct = 0
    ct += 2 * noBehind(n - 1) + oneBehind(n - 2)
    ct += noBehind(n - 2)
    ct += noBehind(n - 3) + oneBehind(n - 4)
    ct += someBehind(n - 3)
    ct %= MOD
    memoSome[n] = ct
    return memoSome[n]


N, M = map(int, input().split())
memoNo = [0] * (N + 1)
memoOne = [0] * (N + 1)
memoTwo = [0] * (N + 1)
memoSome = [0] * (N + 1)

MOD = 1000000007
if M == 1:
    print(1)
elif M == 2:
    arr = [0] * max(3, N + 2)
    arr[1] = 1
    arr[2] = 1
    for i in range(3, N + 1):
        arr[i] = (arr[i - 1] + arr[i - 3]) % MOD
    print(arr[N])
else:
    print(noBehind(N))
# print(memo)
