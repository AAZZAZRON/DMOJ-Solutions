from sys import stdin
from collections import deque
from bisect import bisect_right
input = stdin.readline


def parityX():
    zeroIndex = set()
    for j in range(4):
        if grid[0][j] == 0:
            zeroIndex.add(j)
    for i in grid[1:]:
        for j in range(4):
            if j in zeroIndex and i[j] != 0:
                return False
            elif j not in zeroIndex and i[j] == 0:
                return False
    return testNumbers()


def parityY():
    for i in grid:
        zeroCount = 0
        for j in i:
            if j == 0:
                zeroCount += 1
        if zeroCount == 0 or zeroCount == 4:
            pass
        else:
            return False
    return testNumbers()


def testNumbers():
    global moves
    visited = [[False] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if not visited[i][j]:
                visited[i][j] = True
                queue = deque()
                queue.append([i, j])
                while queue:
                    a, b = queue.popleft()
                    for m, n in moves:
                        x = a + m
                        y = b + n
                        while 0 <= x < 4 and 0 <= y < 4 and grid[x][y] == 0:
                            x += m
                            y += n
                        if 0 <= x < 4 and 0 <= y < 4 and not visited[x][y]:
                            if grid[x][y] != 0 and grid[x][y] == grid[a][b]:
                                return False
                            visited[x][y] = True
                            queue.append([x, y])
    return True


moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
floorList = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
for _ in range(5):
    grid = [[int(x) for x in input().split()] for _ in range(4)]
    if parityX() or parityY():
        maximum = 0
        for i in grid:
            maximum = max(maximum, max(i))
    else:
        maximum = 0
        for i in grid:
            maximum += sum(i)
        maximum = floorList[bisect_right(floorList, maximum) - 1]
    print(maximum)
