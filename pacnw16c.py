from collections import deque

n, k, r = [int(x) for x in input().split()]
cams = [0] * n
for _ in range(k):
    cams[int(input()) - 1] = 1
spots = deque()
t = 0
count = 0
for i in range(r):
    if cams[i]:
        count += 1
    else:
        spots.append(i)
while count < 2:
    cams[spots.pop()] = 1
    count += 1
    t += 1
for i in range(r, n):
    count -= cams[i - r]
    count += cams[i]
    if not cams[i]:
        spots.append(i)
    while count < 2:
        cams[spots.pop()] = 1
        count += 1
        t += 1
print(t)
