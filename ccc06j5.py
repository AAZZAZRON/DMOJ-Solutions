from collections import deque
# -1 = not taken
# 0 = black
# 1 = white


board = [[-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1]]
theInput = input().split()
boardType = theInput[0]
num = int(theInput[1])
b, w = 0, 0
moves = deque([int(x) for x in theInput[2:]])

# initialize the board
if boardType == "a":
    board[4][4] = 1
    board[5][5] = 1
    board[4][5] = 0
    board[5][4] = 0
    b, w = 2, 2
elif boardType == "b":
    for i in range(1, 9):
        board[i][i] = 0
        board[i][9 - i] = 1
    b, w = 8, 8
elif boardType == "c":
    for i in range(1, 9):
        board[i][3] = 0
        board[i][4] = 0
        board[i][5] = 1
        board[i][6] = 1
    b, w = 16, 16

# moves
turn = 0 # who's turn is it
while moves:
    realX = moves.popleft()
    realY = moves.popleft()
    board[realX][realY] = turn
    for i in range(-1, 2): # check all directions
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            x = realX + i
            y = realY + j
            count = 0
            found = False
            while 9 > x > 0 and 9 > y > 0: # make sure no out of bounds
                if board[x][y] == -1:
                    break
                elif board[x][y] != turn:
                    count += 1
                elif board[x][y] == turn:
                    x -= i
                    y -= j
                    found = True
                    break
                x += i
                y += j
            if found:
                while x != realX or y != realY: # increment/decrement counters
                    if turn == 0:
                        board[x][y] = 0
                    else:
                        board[x][y] = 1
                    x -= i
                    y -= j
                if turn == 0:
                    w -= count
                    b += count
                else:
                    w += count
                    b -= count
    if turn == 0:
        b += 1
    else:
        w += 1
    turn = abs(turn - 1)
print(b, w)
