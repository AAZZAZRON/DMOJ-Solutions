n, d = [int(x) for x in input().split()]
line = []
for _ in range(n):
    line.append([int(x) for x in input().split()])
line.sort()
ct = 0
prev = 0
for p, r, g in line:
    ct += p - prev
    tmp = ct % (r + g)
    ct += max(0, r - tmp)
    prev = p
ct += d - prev
print(ct)
