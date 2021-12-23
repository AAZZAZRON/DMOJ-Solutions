import sys
input = sys.stdin.readline


def update(BIT, ind, v):
    while ind <= n:
        BIT[ind] += v
        ind += ind & (-ind)


def query(BIT, ind):
    s = 0
    while ind >= 1:
        s += BIT[ind]
        ind -= ind & (-ind)
    return s


n, q = [int(x) for x in input().split()]
odd = [0] * (n + 1)
even = [0] * (n + 1)
arr = [int(x) for x in input().split()]
for i in range(n):
    if i % 2 == 0:
        update(odd, i + 1, arr[i])
    else:
        update(even, i + 1, arr[i])
for _ in range(q):
    cmd, a, b = [int(x) for x in input().split()]
    if cmd == 1:
        if a % 2 == 0:
            update(even, a, b - arr[a - 1])
        else:
            update(odd, a, b - arr[a - 1])
        arr[a - 1] = b
    else:
        if b % 2 != a % 2:
            b -= 1
        if b % 2 == 0:
            print(query(even, b) - query(even, a - 1))
        else:
            print(query(odd, b) - query(odd, a - 1))