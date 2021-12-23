one = int(input())
two = int(input())
three = int(input())
four = int(input())

if four > three > two > one:
    print('Fish Rising')
elif four < three < two < one:
    print('Fish Diving')
elif one == two == three == four:
    print('Fish At Constant Depth')
else:
    print('No Fish')
