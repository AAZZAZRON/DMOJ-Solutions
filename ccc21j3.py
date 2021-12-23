from sys import stdin
input = stdin.readline


directionBefore = ""
while True:
    one, two, *num = [int(x) for x in input()[:-1]]
    # print(one, two, num)
    if one == two == 9 and num == [9, 9, 9]:
        break
    sum = one + two
    direction = ""
    if sum == 0:
        direction = directionBefore
    elif sum % 2 == 1:
        direction = "left"
        directionBefore = "left"
    elif sum % 2 == 0:
        direction = "right"
        directionBefore = "right"
    print(direction, "".join([str(x) for x in num]))
