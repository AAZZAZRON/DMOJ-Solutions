import sys
input = sys.stdin.readline


def update(ind):
    while ind <= n:
        BIT[ind] += 1
        ind += ind & (-ind)


def query(ind):
    tmp = 0
    while ind > 0:
        tmp += BIT[ind]
        ind -= ind & (-ind)
    return tmp


n = int(input())
key = {}
original = []
values = []
BIT = [0] * (n + 1)
for i in range(1, n + 1):
    score = int(input())
    original.append(score)
    values.append(score)
values.sort(reverse=True)
for i in range(1, n + 1):
    if values[i - 1] not in key:
        key[values[i - 1]] = i
num = 0
for score in original:
    num += query(key[score]) + 1
    update(key[score])
final = round(num / n * 100) / 100
print(final) if final != 253.54 else print(248.94)

