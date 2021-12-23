import sys
input = sys.stdin.readline


def updateN(ind):
    ind += 1
    while ind >= 1:
        NBIT[ind] += 1
        ind -= ind & (-ind)


def queryN(ind):
    tmp = 0
    ind += 1
    while ind <= n:
        tmp += NBIT[ind]
        ind += ind & (-ind)
    return tmp


def updateP(ind):
    ind += 1
    while ind <= n:
        PBIT[ind] += 1
        ind += ind & (-ind)


def queryP(ind):
    ind += 1
    tmp = 0
    while ind >= 1:
        tmp += PBIT[ind]
        ind -= ind & (-ind)
    return tmp


n = int(input())
line = [1 if x == "1" else -1 for x in input().split()]
NBIT = [0] * (n + 1)
PBIT = [0] * (n + 1)
curr = 0
c = 0
for i in line:
    curr += i
    if curr >= 1:
        c += 1
        c += queryN(0)
        c += queryP(curr - 1)
        updateP(curr)
    else:
        c += queryN(-curr + 1)
        updateN(-curr)
print(c)

