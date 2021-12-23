one = int(input())
two = int(input())
three = int(input())
four = int(input())

if one == 8 or one == 9:
    if four == 8 or four == 9:
        if two == three:
            print('ignore')
        else:
            print('answer')
    else:
        print('answer')
else:
    print('answer')
