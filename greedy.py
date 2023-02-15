n, m = [int(x) for x in input().split()]
arr = sorted([[int(x) for x in input().split()] for _ in range(n)])
tot = 0
for p, a in arr:
    if m - a >= 0:
        tot += p * a
        m -= a
    else:
        tot += p * m
        break
print(tot)