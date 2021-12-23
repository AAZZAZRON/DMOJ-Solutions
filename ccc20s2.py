import sys
input = sys.stdin.readline


M = int(input())
N = int(input())
grid = []
for i in range(M):
    grid.append([int(x) for x in input().split()])
book = {}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in book:
            book[grid[i][j]].append((i + 1) * (j + 1))
        else:
            book[grid[i][j]] = [(i + 1) * (j + 1)]
place = grid[-1][-1]
visited = set()
visited.add(M*N)
find = [M*N]
if find[0] == grid[0][0]:
    print("yes")
else:
    while True:
        found = []
        for i in find:
            if i in book:
                found.extend(book[i])
        found = set(found).difference(visited)
        visited |= found
        if grid[0][0] in found:
            print("yes")
            break
        elif not found:
            print("no")
            break
        find = found.copy()
