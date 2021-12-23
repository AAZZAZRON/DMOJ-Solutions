import sys
input = lambda: sys.stdin.readline()[:-1]


alpha = {}
a = "abcdefghijklmnopqrstuvwxyz "
for i in range(27):
    alpha[a[i]] = i
line = input()
length = len(line)
psa = [[0] * (length + 1) for _ in range(26)]
for i in range(length):
    for j in range(26):
        if alpha[line[i]] == j:
            psa[j][i] = psa[j][i - 1] + 1
        else:
            psa[j][i] = psa[j][i - 1]
for _ in range(int(input())):
    l, r, q = input().split()
    print(psa[alpha[q]][int(r) - 1] - psa[alpha[q]][int(l) - 2])
