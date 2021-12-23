r, c = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(r)]
for i in range(int(input())):
    t = int(input())
    grid = sorted(grid, key=lambda x: x[t - 1])
[print(" ".join([str(x) for x in i])) for i in grid]
