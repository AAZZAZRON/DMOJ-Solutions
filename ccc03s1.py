import sys
input = sys.stdin.readline


player = 1
while True:
    move = int(input())
    if move == 0:
        print("You Quit!")
        break
    player += move
    if player == 9:
        player = 34
    elif player == 40:
        player = 64
    elif player == 67:
        player = 86
    elif player == 54:
        player = 19
    elif player == 90:
        player = 48
    elif player == 99:
        player = 77
    elif player > 100:
        player -= move
    print("You are now on square", player)
    if player == 100:
        print("You Win!")
        break
