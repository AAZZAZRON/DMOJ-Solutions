n, s = [int(x) for x in input().split()]
line = input()
ct = 0
for q in range(n):
    i = line[q]
    if i == "U" and s != 0:
        s -= 1
    elif i == "D":
        s += 1
    if s == 0:
        ct += 1
print(ct)