import sys
from bisect import bisect_right
input = sys.stdin.readline


n = int(input())
strengths = [int(x) for x in input().split()]
psa = [0]
for i in strengths:
    psa.append(psa[-1] + i)
inc = 0
total = psa[-1]
# print(psa)
ind = bisect_right(psa, total // 2 + inc)
one = total - psa[ind - 1] + inc
two = total - psa[ind] + inc
print(min(abs(one - total + one), abs(two - total + two)), end= " ")
for i in range(n - 1):
    psa.append(psa[-1] + strengths[i])
    inc += strengths[i]
    ind = bisect_right(psa, total // 2 + inc)
    one = total - psa[ind - 1] + inc
    two = total - psa[ind] + inc
    # print(psa, ind, total // 2 + inc, inc, psa[ind - 1], psa[ind], one, two)
    if i == n - 2:
        print(min(abs(one - total + one), abs(two - total + two)))
    else:
        print(min(abs(one - total + one), abs(two - total + two)), end=" ")
