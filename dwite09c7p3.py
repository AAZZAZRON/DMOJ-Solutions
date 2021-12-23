def check(x, y):
    containOil = []
    if globe[x + 1][y] == "#":
        containOil.append([x + 1, y])
    if globe[x - 1][y] == "#":
        containOil.append([x - 1, y])
    if globe[x][y + 1] == "#":
        containOil.append([x, y + 1])
    if globe[x][y - 1] == "#":
        containOil.append([x, y - 1])
    for i in containOil:
        if i not in alreadyFound:
            alreadyFound.append(i)
            count.append(1)
            check(i[0], i[1])


for i in range(0, 5):
    globe = []
    alreadyFound = []
    count = [1]
    for j in range(0, 10):
        x = input()
        if "A" in x:
            A = [j, x.index("A")]
        globe.append(x)
    x = input()
    check(A[0], A[1])
    print(len(count))
