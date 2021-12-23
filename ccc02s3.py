import sys
input = sys.stdin.readline


def runThrough(place, rotate):
    global coord
    for move in moves:
        if move == "F":
            place = [place[0] + movement[rotate][0], place[1] + movement[rotate][1]]
            if x <= place[0] or place[0] < 0 or y <= place[1] or place[1] < 0:
                return False
            elif grid[place[0]][place[1]] == "X":
                return False
        elif move == "L":
            rotate -= 1
        elif move == "R":
            rotate += 1
        rotate %= 4
    coord = place
    return True


movement = [[-1, 0], [0, 1], [1, 0], [0, -1]]
x = int(input())
y = int(input())
grid = [[x for x in input()[:-1]] for i in range(x)]
numMoves = int(input())
moves = [input()[:-1] for j in range(numMoves)]
for i in range(x):
    for j in range(y):
        if grid[i][j] == "." or grid[i][j] == "*":
            for d in range(4):
                coord = []
                if runThrough([i, j], d):
                    grid[coord[0]][coord[1]] = "*"
[print("".join(grid[q])) for q in range(x)]
