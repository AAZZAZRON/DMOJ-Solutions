def output(inputs):
    for i in inputs:
        printed = ""
        for j in i:
            printed += str(j) + " "
        printed = printed[:-1]
        print(printed)
    return


low = int(input())
high = int(input()) + 1
list = [[low]]
num = low + 1
direction = "down"
stop = False
while True:
    if direction == "down":
        for x in range(1, len(list)):
            if num == high:
                stop = True
                break
            list[x].insert(0, num)
            num += 1
        if num == high:
            stop = True
        else:
            lists = [num]
            num += 1
            list.append(lists)
            direction = "right"
    elif direction == "right":
        for x in range(1, len(list[0]) + 1):
            if num == high:
                stop = True
                break
            list[-1].append(num)
            num += 1
        direction = "up"
    elif direction == "up":
        for x in range(2, len(list) + 1):
            if num == high:
                stop = True
                break
            list[-x].append(num)
            num += 1
        if num == high:
            stop = True
        else:
            lists = [num]
            num += 1
            list.insert(0, lists)
            direction = "left"
    elif direction == "left":
        for x in range(1, len(list[1]) + 1):
            if num == high:
                stop = True
                break
            list[0].insert(0, num)
            num += 1
            x += 1
        direction = "down"
    if stop:
        output(list)
        break
