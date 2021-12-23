from sys import stdin
input = stdin.readline


col, row = [int(x) for x in input().split()]
cannotGo = set()
for i in range(col):
    x = input()
    before = 0
    while x[before:].count("#") != 0:
        index = x[before:].index("#") + before
        before = index + 1
        cannotGo.add((i, index))
walk = [0] * row
walkThrough = [(walk.copy()) for i in range(col)]
walkThrough[0][0] = 1
for i in range(col):
    for j in range(row):
        if (i, j) in cannotGo:
            continue
        if i + 1 != col:
            walkThrough[i + 1][j] += walkThrough[i][j]
        if j + 1 != row:
            walkThrough[i][j + 1] += walkThrough[i][j]
print(walkThrough[-1][-1] % 1000000007)
