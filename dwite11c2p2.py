import sys
input = lambda: sys.stdin.readline()[:-1]


for _ in range(5):
    r, c = [int(x) for x in input().split()]
    grid = ""
    for _ in range(r):
        grid += input()
    key = input()
    ind = 0
    new = ""
    length = len(key)
    for i in grid:
        if ind != length and i == key[ind]:
            new += "."
            ind += 1
        else:
            new += "#"
    if ind == length:
        for i in range(0, r * c, c):
            print(new[i:i + c])
    else:
        for i in range(r):
            print("x" * c)
