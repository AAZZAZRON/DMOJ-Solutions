import sys
import bisect
input = lambda: sys.stdin.readline()[:-1]


n = int(input())
lines = [{} for _ in range(n)]
for i in range(n):
    x = input()
    for j in range(len(x)):
        ind = ord(x[j]) - ord('a')
        if ind in lines[i]:
            lines[i][ind].append(j)
        else:
            lines[i][ind] = [j]
inds = [0] * n
lst = [0] * n
final = ""
for l in range(25, -1, -1):
    c = 1000001
    for i in range(n):
        if l not in lines[i] or c == 0:
            c = 0
            break
        ind = bisect.bisect_left(lines[i][l], inds[i])
        c = min(c, len(lines[i][l]) - ind)
        lst[i] = ind - 1
    if c > 0:
        final += (chr(l + ord('a'))) * c
        for j in range(n):
            inds[j] = lines[j][l][lst[j] + c] + 1
if final == "":
    print(-1)
else:
    print(final)
