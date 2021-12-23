from math import ceil

y, x = [int(x) for x in input().split()]
counter = 0
coords = []
before = 1
for i in range(1, y + 1):
    whole = False
    value = i * x / y
    if value // 1 == value:
        whole = True
    value = ceil(value)
    for j in range(before, value + 1):
        counter += 1
        coords.append(str(i) + " " + str(j))
    before = value
    if whole:
        before += 1
print(counter)
[print(x) for x in coords]