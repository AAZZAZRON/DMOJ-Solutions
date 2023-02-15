from collections import defaultdict
f = defaultdict(int)
for i in input():
    f[i] += 1
v = sorted(f.values())
print(sum(v[:-2]))