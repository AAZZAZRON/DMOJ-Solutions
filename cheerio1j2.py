n, t = [int(x) for x in input().split()]
name, c = "", 10**12
for _ in range(n):
    a, b = input().split()
    if abs(t - int(b)) < c:
        c = abs(t - int(b))
        name = a
print(name)
