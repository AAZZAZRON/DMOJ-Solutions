n, k = [int(x) for x in input().split()]
total = 0
save = []
for _ in range(n):
    d, p = [int(x) for x in input().split()]
    total += d
    save.append(d - p)
save.sort()
if k == 0:
    print(total)
else:
    print(total - sum(save[-k:]))
