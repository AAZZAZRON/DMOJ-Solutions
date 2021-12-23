import sys
sys.setrecursionlimit(150001)
input = sys.stdin.readline


def travel(cX, cY, len=0):
    global maximum
    length = 0
    if memo[cX][cY] != 0:
        return memo[cX][cY] + len
    for i, j in moves:
        if 0 <= cX + i < dim and 0 <= cY + j < dim and grid[cX + i][cY + j] > grid[cX][cY]:
            length = max(length, travel(cX + i, cY + j, len + 1) - len)
    memo[cX][cY] = length
    if length > maximum:
        maximum = length
    return length + len


dim = int(input())
grid = [[int(x) for x in input().split()] for i in range(dim)]
# print(grid)
smallT = [0] * dim
memo = [smallT.copy() for _ in range(dim)]
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
maximum = 0
for x in range(dim - 1, -1, -1):
    for y in range(dim - 1, -1, -1):
        travel(x, y)
print(maximum)
