size = int(input())
if size % 2 == 1:
    num = 1
    for i in range(size):
        grid = []
        for j in range(size):
            grid.append(str(num))
            num += 1
        print(" ".join(grid))
elif size == 2:
    print(-1)
else:
    lastTotal = []
    num = 1
    for i in range(size):
        if i == size - 1:
            num = lastTotal[-1] * size - sum(lastTotal)
        grid = []
        for j in range(size - 1):
            if j == 0:
                lastTotal.append(num)
            grid.append(num)
            num += 1
        grid.append(grid[-1] * size - sum(grid))
        num = grid[-1] + 1
        print(" ".join(str(x) for x in grid))
