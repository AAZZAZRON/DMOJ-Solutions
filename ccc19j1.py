a_three = int(input())
a_two = int(input())
a_one = int(input())
b_three = int(input())
b_two = int(input())
b_one = int(input())

a_equation = 3 * a_three + 2 * a_two + a_one
b_equation = 3 * b_three + 2 * b_two + b_one

if a_equation > b_equation:
    print('A')
elif b_equation > a_equation:
    print('B')
else:
    print('T')

