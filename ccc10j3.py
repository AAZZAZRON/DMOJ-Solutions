inputList = []
while True:
    x = input()
    if x == '7':
        break
    else:
        xSplit = x.split()
        y = []
        for i in range(0, len(xSplit)):
            y.append(xSplit[i])
        inputList.append(y)

X = 0
Y = 0

for i in range(0, len(inputList)):
    action = inputList[i]
    z = 0
    if action[0] == '1':
        if action[1] == 'A':
            X = int(action[2])
        else:
            Y = int(action[2])
    elif action[0] == '2':
        if action[1] == 'A':
            print(X)
        else:
            print(Y)
    elif action[0] == '3':
        one = action[1]
        two = action[2]
        if one == 'A' and two == 'A':
            z = X + X
        elif one == 'A' and two == 'B':
            z = X + Y
        elif one == 'B' and two == 'A':
            z = Y + X
        else:
            z = Y + Y
        if action[1] == 'A':
            X = z
        else:
            Y = z
    elif action[0] == '4':
        one = action[1]
        two = action[2]
        if one == 'A' and two == 'A':
            z = X * X
        elif one == 'A' and two == 'B':
            z = X * Y
        elif one == 'B' and two == 'A':
            z = Y * X
        else:
            z = Y * Y
        if action[1] == 'A':
            X = z
        else:
            Y = z
    elif action[0] == '5':
        one = action[1]
        two = action[2]
        if one == 'A' and two == 'A':
            z = X - X
        elif one == 'A' and two == 'B':
            z = X - Y
        elif one == 'B' and two == 'A':
            z = Y - X
        else:
            z = Y - Y
        if action[1] == 'A':
            X = z
        else:
            Y = z
    elif action[0] == '6':
        one = action[1]
        two = action[2]
        if one == 'A' and two == 'A':
            z = X // X
        elif one == 'A' and two == 'B':
            z = X // Y
        elif one == 'B' and two == 'A':
            z = Y // X
        else:
            z = Y // Y
        if action[1] == 'A':
            X = z
        else:
            Y = z
    else:
        print('Hello')
