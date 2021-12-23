maxR, maxC = [int(x) for x in input().split()]
one, two = 0, 0
while True:
    add, added = [int(x) for x in input().split()]
    if add == added == 0:
        break
    one += add
    two += added
    if one > maxR:
        one = maxR
    elif one < 0:
        one = 0
    if two > maxC:
        two = maxC
    elif two < 0:
        two = 0
    print(one, two)
