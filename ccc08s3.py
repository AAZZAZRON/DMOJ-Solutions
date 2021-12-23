import sys
input = sys.stdin.readline


def findMinimum(canGoTo, count=1):
    global visited
    if grid[rows - 1][columns - 1] == "*":
        print(-1)
        return
    while True:
        if f"{rows - 1}x{columns - 1}" in visited:
            print(count)
            break
        if not canGoTo:
            print(-1)
            break
        next = []
        for w in canGoTo:
            w = w.split("x")
            q = [int(x) for x in w]
            direction = grid[q[0]][q[1]]
            if direction == "|" or direction == "+":
                if q[0] + 1 != rows:
                    next.append(f"{q[0] + 1}x{q[1]}")
                if q[0] - 1 != -1:
                    next.append(f"{q[0] - 1}x{q[1]}")
            if direction == "-" or direction == "+":
                if q[1] + 1 != columns:
                    next.append(f"{q[0]}x{q[1] + 1}")
                if q[1] - 1 != -1:
                    next.append(f"{q[0]}x{q[1] - 1}")
        canGoTo = list(set(next).difference(set(visited)))
        visited |= set(canGoTo)
        count += 1


numCases = int(input())
for i in range(numCases):
    visited = set()
    visited.add("0x0")
    grid = []
    rows = int(input())
    columns = int(input())
    for j in range(rows):
        line = [x for x in input()]
        grid.append(line)
    findMinimum(["0x0"])
