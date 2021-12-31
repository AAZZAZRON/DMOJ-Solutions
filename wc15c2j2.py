n, m = [int(x) for x in input().split()]
ct = 0
for _ in range(n):
    v = int(input())
    if v <= m:
        ct += v
print(ct)