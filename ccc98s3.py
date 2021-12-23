import sys
input = sys.stdin.readline


def goHorizontal():
    global facing
    # print("H", horizontal, facing)
    if horizontal > 0:
        if facing % 4 == 0:
            print(3)
            facing -= 1
        elif facing % 4 == 2:
            print(2)
            facing += 1
        elif facing % 4 == 1:
            print(2)
            print(2)
            facing += 2
    elif horizontal < 0:
        if facing % 4 == 0:
            print(2)
            facing += 1
        elif facing % 4 == 2:
            print(3)
            facing -= 1
        elif facing % 4 == 3:
            print(2)
            print(2)
            facing += 2
    print(1)
    print(abs(horizontal))
    return


def goVertical():
    global facing
    # print("V", vertical, facing)
    if vertical > 0:
        if facing % 4 == 1:
            print(2)
            facing += 1
        elif facing % 4 == 3:
            print(3)
            facing -= 1
        elif facing % 4 == 0:
            print(2)
            print(2)
            facing += 2
    elif vertical < 0:
        if facing % 4 == 3:
            print(2)
            facing += 1
        elif facing % 4 == 1:
            print(3)
            facing -= 1
        elif facing % 4 == 2:
            print(2)
            print(2)
            facing += 2
    print(1)
    print(abs(vertical))
    return


numTimes = int(input())
for i in range(numTimes):
    horizontal, vertical = 0, 0
    facing = 0
    while True:
        move = int(input())
        if move == 1:
            amount = int(input())
            if facing % 4 == 0: # up
                vertical += amount
            elif facing % 4 == 2: # down
                vertical -= amount
            elif facing % 4 == 3: # left
                horizontal -= amount
            elif facing % 4 == 1: # right
                horizontal += amount
        elif move == 2:
            facing += 1
        elif move == 3:
            facing -= 1
        else:
            break
    total = abs(horizontal) + abs(vertical)
    print(f"Distance is {total}")
    # print(horizontal, vertical)
    if total != 0:
        verticalGo = -1
        if vertical > 0:
            verticalGo = 2
        elif vertical < 0:
            verticalGo = 0
        horizontalGo = -1
        if horizontal > 0:
            horizontalGo = 3
        elif horizontal < 0:
            horizontalGo = 1 # declare directions of the horizontal and vertical
        if horizontal == 0:
            goVertical()
        elif vertical == 0:
            goHorizontal()
        elif facing % 2 == 0 and facing % 4 == verticalGo:
            goVertical()
            goHorizontal()
        elif facing % 2 == 0 and facing % 4 != verticalGo:
            goHorizontal()
            goVertical()
        elif facing % 2 == 1 and facing % 4 == horizontalGo:
            goHorizontal()
            goVertical()
        elif facing % 2 == 1 and facing % 4 != horizontalGo:
            goVertical()
            goHorizontal()
