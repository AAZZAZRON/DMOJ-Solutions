import sys
input = sys.stdin.readline


rows, columns = [int(x) for x in input().split()]
room = []
visited = set()
queue = []
counter = 0
values = {}
cameras = set()
cameraSquares = []
movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
done = False
for i in range(rows):
    small = input()[:-1]
    if "S" in small:
        visited.add((i, small.index("S")))
        queue.append([[i, small.index("S")]])
    ind = 0
    while small[ind:].count("C") != 0:
        place = small[ind:].index("C")
        cameraSquares.append((i, place + ind))
        ind += place + 1
    room.append(small)
for start in cameraSquares:
    cameras.add(start)
    for x in movement:
        camera = start
        while True:
            camera = (camera[0] + x[0], camera[1] + x[1])
            symbol = room[camera[0]][camera[1]]
            if symbol == "W":
                break
            elif symbol == ".":
                cameras.add(camera)
            elif symbol == "S":
                done = True
                break
if not done:
    while queue:
        counter += 1
        moves = queue[0]
        queue = []
        add = []
        for coord in moves:
            for i, j in movement:
                new = (coord[0] + i, coord[1] + j)
                while True:
                    if new in visited or new in cameras:
                        break
                    spot = room[new[0]][new[1]]
                    visited.add(new)
                    if spot == ".":
                        add.append(new)
                        values[tuple(new)] = counter
                        break
                    elif spot == "W":
                        break
                    elif spot == "U":
                        new = (new[0] - 1, new[1])
                    elif spot == "D":
                        new = (new[0] + 1, new[1])
                    elif spot == "L":
                        new = (new[0], new[1] - 1)
                    elif spot == "R":
                        new = (new[0], new[1] + 1)
                    spot = room[new[0]][new[1]]

        if add:
            queue.append(add)

for i in range(rows):
    row = room[i]
    ind = 0
    while row[ind:].count(".") != 0:
        place = row[ind:].index(".")
        if (i, place + ind) not in values:
            print(-1)
        else:
            print(values[(i, place + ind)])
        ind += place + 1
