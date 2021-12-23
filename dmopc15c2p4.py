import sys
from bisect import bisect_left
input = sys.stdin.readline


def update(ind, val):
    while ind > 0:
        BIT[ind] = max(BIT[ind], val)
        ind -= ind & (-ind)


def getMax(ind):
    global num
    tmp = 0
    while ind <= num:
        tmp = max(tmp, BIT[ind])
        ind += ind & (-ind)
    return tmp


num = int(input())
maximum = 0
BIT = [0] * (num + 2)
anime = [[int(x) for x in input().split()] for _ in range(num)]
# let dp[i] be the maximum amount of happiness points
# if we start watching by watching anime[i]
for i in range(num - 1, -1, -1):
    a, b, c = anime[i]
    opt = getMax(bisect_left(anime, [a + b, 0, 0])) + c
    update(i, opt)
    maximum = max(maximum, opt)
print(maximum)
