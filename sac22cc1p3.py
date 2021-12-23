import sys
input = lambda: sys.stdin.readline()[:-1]


r, c = [int(x) for x in input().split()]
grid = [[x for x in input()] for i in range(r)]
moved = [[0] * c for _ in range(r)]
grid.append([''] * c)
for q in range(int(input())):
    if int(input()) == 1:
        for i in range(r - 1, -1, -1):
            for j in range(c):
                if grid[i][j] == "X":
                    grid[i + 1][j] = "X"
                    grid[i][j] = "."
        done = 0
        while not done:
            done = 1
            for i in range(r):
                ind = 0
                for j in range(c):
                    if grid[i][j] == "W" and ind != j:
                        grid[i][j] = "."
                        grid[i][ind] = "W"
                        ind += 1
                        done = 0
                    if grid[i][j] == "X" or grid[i][j] == "W":
                        ind = j + 1
            for i in range(r - 1):
                for j in range(c):
                    if not moved[i][j] and grid[i][j] == "W" and grid[i + 1][j] == ".":
                        grid[i][j] = "."
                        grid[i + 1][j] = "W"
                        moved[i + 1][j] = 1
                        done = 0
                    moved[i][j] = 0
    else:
        [print("".join(x)) for x in grid[:-1]]
