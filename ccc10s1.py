v = []
for _ in range(int(input())):
    name, r, s, d = input().split()
    val = int(r) * 2 + int(s) * 3 + int(d)
    v.append([-val, name])
v.sort()
if len(v) == 0:
    print()
elif len(v) == 1:
    print(v[0][1])
else:
    print(v[0][1])
    print(v[1][1])