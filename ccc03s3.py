import sys
input = sys.stdin.readline


def search(coord):
    area = 1
    visit.append(coord)
    queue.append(coord)
    while queue:
        x, y = queue.pop(0)
        if x != 0 and [x - 1, y] not in visit:
            if floor[x - 1][y] == ".":
                queue.append([x - 1, y])
                area += 1
            visit.append([x - 1, y])
        if y != 0 and [x, y - 1] not in visit:
            if floor[x][y - 1] == ".":
                queue.append([x, y - 1])
                area += 1
            visit.append([x, y - 1])
        if x != len(floor) - 1 and [x + 1, y] not in visit:
            if floor[x + 1][y] == ".":
                queue.append([x + 1, y])
                area += 1
            visit.append([x + 1, y])
        if y != len(floor[0]) - 1 and [x, y + 1] not in visit:
            if floor[x][y + 1] == ".":
                queue.append([x, y + 1])
                area += 1
            visit.append([x, y + 1])
    return area


floor = []
areas = []
woodAmount = int(input())
row = int(input())
col = int(input())
for i in range(row):
    floor.append(input()[:-1])
bigVisit = []
for i in range(row):
    for j in range(col):
        if floor[i][j] == "." and [i, j] not in bigVisit:
            visit = []
            queue = []
            areas.append(search([i, j]))
            bigVisit += visit
areas.sort()
areas.reverse()
areas.append(50000098134098123048102348019234012398401928340918234)
roomsFilled = 0
while woodAmount - areas[0] >= 0:
    roomsFilled += 1
    woodAmount -= areas[0]
    areas.pop(0)
if roomsFilled == 1:
    print("{} room, {} square metre(s) left over".format(roomsFilled, woodAmount))
else:
    print("{} rooms, {} square metre(s) left over".format(roomsFilled, woodAmount))
