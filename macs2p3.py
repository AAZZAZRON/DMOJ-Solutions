from bisect import bisect_left
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = [int(x) for x in input().split()]
psa = [0] * (n + 1)
for i in range(1, n + 1):
    psa[i] = psa[i - 1] + arr[i - 1]
# psa[-1] = 10 ** 14
# print(psa)
for _ in range(q):
    cmd, l, s = input().split()
    l = int(l)
    s = int(s)
    ind = bisect_left(psa, s + psa[l - 1])
    if ind == n + 1:
        ind -= 1
    print(ind)