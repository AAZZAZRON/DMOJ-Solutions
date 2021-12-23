import sys
input = sys.stdin.readline


r, c, area = [int(x) for x in input().split()]
psa = [[0] * (r + 1) for _ in range(c + 1)]
for i in range(1, c + 1):
    line = [int(x) for x in input().split()]
    total = 0
    for j in range(1, r + 1):
        total += line[j - 1]
        psa[i][j] = total + psa[i - 1][j]
# [print(x) for x in psa]
maximum = 0
for l in range(1, min(c + 1, area + 1)):
    w = min(r, area // l)
    for i in range(l, c + 1):
        for j in range(w, r + 1):
            maximum = max(maximum, psa[i][j] - psa[i - l][j] - psa[i][j - w] + psa[i - l][j - w])
print(maximum)
