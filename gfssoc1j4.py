board = []
for i in range(3):
    row = [x for x in input()]
    board.append(row)
G, T = False, False
for i in range(0, 3):
    for j in range(0, 3):
        if i == 0 and j == 0:
            if board[i][j] == board[i][j + 1] == board[i][j + 2] or board[i][j] == board[i + 1][j] == board[i + 2][j]:
                if board[i][j] == "O":
                    G = True
                else:
                    T = True
        elif i == 2 and j == 2:
            if board[i][j] == board[i][j - 1] == board[i][j - 2] or board[i][j] == board[i - 1][j] == board[i - 2][j]:
                if board[i][j] == "O":
                    G = True
                else:
                    T = True
        elif i == 1 and j == 1:
            if board[i - 1][j - 1] == board[i][j] == board[i + 1][j + 1]:
                if board[i][j] == "O":
                    G = True
                else:
                    T = True
            elif board[i][j - 1] == board[i][j] == board[i][j + 1]:
                if board[i][j] == "O":
                    G = True
                else:
                    T = True
            elif board[i - 1][j] == board[i][j] == board[i + 1][j]:
                if board[i][j] == "O":
                    G = True
                else:
                    T = True
            elif board[i + 1][j - 1] == board[i][j] == board[i - 1][j + 1]:
                if board[i][j] == "O":
                    G = True
                else:
                    T = True
if G and T:
    print("Error, redo")
elif G:
    print("Griffy")
elif T:
    print("Timothy")
else:
    print("Tie")
