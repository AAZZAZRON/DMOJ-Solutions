"""
Given two coordinates on an 8x8 grid, output the amount of moves it takes to get there
given the piece can only move using the knight's move
"""


def KnightsMove(X, Y):
    count = 0
    make = 8
    bigCount = 0
    done = False
    visited.append([X, Y])
    queue.append([X, Y])
    while queue and not done:
        s = queue.pop(0)
        for i in possibleMoves:
            placeX, placeY = s[0] + i[0], s[1] + i[1]
            if placeX == endX and placeY == endY:
                print(bigCount + 1)
                done = True
                break
            if 0 < placeX <= 8 and 0 < placeY <= 8 and [placeX, placeY] not in visited:
                visited.append([placeX, placeY])
                queue.append([placeX, placeY])
                count += 1
            else:
                make -= 1
        if count == make:
            bigCount += 1
            count = 0
            make *= 8


# possible moves
possibleMoves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
board = [1, 2, 3, 4, 5, 6, 7, 8]

# getting the input
startX, startY = [int(x) for x in input().split()]
endX, endY = [int(x) for x in input().split()]
visited = []
queue = []
if [startX, startY] == [endX, endY]:
    print(0)
else:
    KnightsMove(startX, startY)
