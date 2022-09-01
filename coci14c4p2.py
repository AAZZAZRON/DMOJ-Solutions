import sys
input = sys.stdin.readline
from collections import deque, defaultdict
n = int(input())
arr = sorted([int(x) for x in input().split()])
f = defaultdict(int)
for i in arr:
    f[i] += 1
d = deque()
for i in f:
    d.append([i, f[i]])
# print(d)
pt = 1
while len(d) > 2:
    # print(d)
    if d[0][1] < d[-1][1]:
        d[-1][1] -= d[0][1]
        d[-2][1] += d[0][1]
        d[1][1] += d[0][1]
        d.popleft()
        pt = 0
    elif d[0][1] == d[-1][1]:
        d[1][1] += d[0][1]
        d[-2][1] += d[-1][1]
        d.pop()
        d.popleft()
    else:
        d[0][1] -= d[-1][1]
        d[1][1] += d[-1][1]
        d[-2][1] += d[-1][1]
        d.pop()
        pt = 1
# print(d)
print("Slavko" if pt % 2 == 1 else "Mirko")
if len(d) == 1:
    print(d[0][0], d[0][0])
else:
    print(d[0][0], d[1][0])
