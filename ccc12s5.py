from sys import stdin
input = stdin.readline


row, col = [int(x) for x in input().split()]
times = int(input())
cannotGo = set()
for i in range(times):
    cannotGo.add(tuple([int(x) - 1 for x in input().split()]))
travel = [0] * col
mouse = [(travel.copy()) for i in range(row)]
mouse[0][0] = 1
for i in range(row):
    for j in range(col):
        if (i, j) in cannotGo:
            continue
        if i + 1 != row:
            mouse[i + 1][j] += mouse[i][j]
        if j + 1 != col:
            mouse[i][j + 1] += mouse[i][j]
print(mouse[-1][-1] % 1000000000)
