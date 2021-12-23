import sys
input = sys.stdin.readline


def solve(l, r, v):
    if r <= l:
        return 0
    c = min(arr[l:r])
    ind = arr[l:r].index(c) + l
    c -= v
    c += solve(l, ind, v + c) + solve(ind + 1, r, v + c)
    return c


n = int(input())
arr = [int(x) for x in input().split()]
print(solve(0, n, 0))
