hole = [[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], [3, -3], [3, -4], [4, -5], [4, -5], [5, -5], [5, -4], [5, -3], [6, -3], [7, -3], [7, -4], [7, -5], [7, -6], [7, -7], [6, -7], [5, -7], [4, -7], [3, -7], [2, -7], [1, -7], [0, -7], [-1, -7], [-1, -6], [-1, -5]]
x = 0
last = [-1, -5]
for a in range(0, 1000000):
    command = input()
    cSplit = command.split()
    direction = cSplit[0]
    amount = int(cSplit[1])
    if direction == 'l':
        z = 0
        for i in range(0, amount):
            last[0] -= 1
            lastly = last.copy()
            hole.append(lastly)
            count = hole.count(lastly)
            if count >= 2:
                z = 1
        if z == 1:
            print(last[0], last[1], 'DANGER')
            break
        else:
            print(last[0], last[1], 'safe')
    elif direction == 'r':
        z = 0
        for i in range(0, amount):
            last[0] += 1
            lastly = last.copy()
            hole.append(lastly)
            count = hole.count(lastly)
            if count >= 2:
                z = 1
        if z == 1:
            print(last[0], last[1], 'DANGER')
            break
        else:
            print(last[0], last[1], 'safe')
    elif direction == 'u':
        z = 0
        for i in range(0, amount):
            last[1] += 1
            lastly = last.copy()
            hole.append(lastly)
            count = hole.count(lastly)
            if count >= 2:
                z = 1
        if z == 1:
            print(last[0], last[1], 'DANGER')
            break
        else:
            print(last[0], last[1], 'safe')
    elif direction == 'd':
        z = 0
        for i in range(0, amount):
            last[1] -= 1
            lastly = last.copy()
            hole.append(lastly)
            count = hole.count(lastly)
            if count >= 2:
                z = 1
        if z == 1:
            print(last[0], last[1], 'DANGER')
            break
        else:
            print(last[0], last[1], 'safe')
    else:
        break
    if z == 1:
        break
