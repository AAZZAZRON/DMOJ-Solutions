image = [['*', 'x', '*'],
         [' ', 'x', 'x'],
         ['*', ' ', '*']]
scale = int(input())

for i in range(0, 3):
    one = image[i][0]
    two = image[i][1]
    three = image[i][2]
    x = ''
    x = x + one*scale + two* scale + three * scale
    for j in range(0, scale):
        print(x)
