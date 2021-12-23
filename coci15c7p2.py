import sys
input = sys.stdin.readline


row, column, length = [int(x) for x in input().split()]
grid = []
flies = []
for i in range(row):
    x = input()
    grid.append(x[:-1])
    x = "!" + x + "!"
    if x.count("*") != 0:
        while x.count("*") != 0:
            index = x.index("*")
            flies.append([i, index - 1])
            x = x[:index] + "." + x[index + 1:]
max = 0
corner = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if j + length - 1 < column and i + length - 1 < row:
            count = 0
            for fly in flies:
                if i < fly[0] <= i + length - 2 and j < fly[1] <= j + length - 2:
                    count += 1
            if count > max:
                max = count
                corner = [i, j]
print(max)
change = False
times = 0
for i in range(len(grid)):
    r = grid[i] + "!"
    if change:
        if times == length - 2:
            r = r[:corner[1]] + "+" + "-" * (length - 2) + "+" + r[corner[1] + length:]
            change = False
        else:
            r = r[:corner[1]] + "|" + r[corner[1] + 1:corner[1] + length - 1] + "|" + r[corner[1] + length:]
            times += 1
    if i == corner[0]:
        r = r[:corner[1]] + "+" + "-" * (length - 2) + "+" + r[corner[1] + length:]
        change = True
    print(r[:-1])
