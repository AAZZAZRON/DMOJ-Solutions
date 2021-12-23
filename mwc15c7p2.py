import sys
input = sys.stdin.readline

f, r = [int(x) for x in input().split()]
psa = [[0] * (r + 1) for _ in range(f + 1)]
for i in range(1, f + 1):
    line = [int(x) for x in input().split()]
    for j in range(1, r + 1):
        psa[i][j] = psa[i][j - 1] + line[j - 1]
for _ in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    print(psa[c][b] - psa[c][a - 1])