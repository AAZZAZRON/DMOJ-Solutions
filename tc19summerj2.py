n, m = [int(x) for x in input().split()]
ct = 0
last = 0
for _ in range(n):
    v = int(input())
    if v == 0 and last == 1:
        ct += 1
    last = v
if last == 1:
    ct += 1
print(ct)