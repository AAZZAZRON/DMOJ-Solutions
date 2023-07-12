n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(2)]

ct = 0
for i in range(n):
    if grid[0][i]:
        ct += 3
        if i - 1 >= 0 and grid[0][i - 1]:
            ct -= 2
for i in range(n):
    if grid[1][i]:
        ct += 3
        if i - 1 >= 0 and grid[1][i - 1]:
            ct -= 2
        if i % 2 == 0 and grid[0][i]:
            ct -= 2
print(ct)