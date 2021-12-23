from sys import stdin
input = stdin.readline


tests = int(input())
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(tests):
    r, c = [int(x) for x in input().split()]
    house = []
    start = [0, 0]
    foundStart = False
    for q in range(c):
        side = [x for x in input()[:-1]]
        if not foundStart:
            try:
                index = side.index("C")
                start = [q, index]
                foundStart = True
            except ValueError:
                pass
        house.append(side)
    if not foundStart:
        print("#notworth")
        continue
    visited = {tuple(start)}
    queue = [[start]]
    counter = 0
    solved = False
    while queue and counter < 59 and not solved:
        counter += 1
        queued = queue.pop()
        added = []
        for a, b in queued:
            for x, y in moves:
                x += a
                y += b
                if 0 <= x < c and 0 <= y < r and (x, y) not in visited and house[x][y] != "X":
                    if house[x][y] == "W":
                        solved = True
                        break
                    visited.add((x, y))
                    added.append([x, y])
                if solved:
                    break
            if solved:
                break
        if added:
            queue.append(added)
    if solved:
        print(counter)
    else:
        print("#notworth")
