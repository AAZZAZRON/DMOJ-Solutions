one = int(input())
two = int(input())
three = int(input())

if one + two + three != 180:
    print('Error')
else:
    if one == two == three:
        print('Equilateral')
    elif one == two or two == three or one == three:
        print('Isosceles')
    else:
        print('Scalene')
