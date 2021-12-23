from sys import stdin
input = stdin.readline


for _ in range(5):
    counter = 0
    num = int(input())
    grid = [input()[:-1] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            if grid[i][j] == ".":
                continue
            size = 0
            nextLayer = True
            while nextLayer:
                nextLayer = False
                counter += 1
                size += 1
                if 0 <= j - size < num and 0 <= j + size < num and i + size < num:
                    if grid[i + size][j - size:j + size + 1] == "#" * (2 * size + 1):
                        nextLayer = True
    print(counter)
