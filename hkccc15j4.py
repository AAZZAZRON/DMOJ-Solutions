l = int(input())
n = int(input())
sweep = []
sweep.append([l, 1])
for i in range(n):
    a, b = [int(x) for x in input().split()]
    sweep.append([a, 1])
    sweep.append([b, -1])
sweep.sort()

m = 0
prev = 0
ct = 0
for a, b in sweep:
    if ct == 0:
        m = max(m, a - prev)
    ct += b
    prev = a
print(m)
