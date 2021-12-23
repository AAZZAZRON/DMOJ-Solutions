first = input()
second = input()
third = input()
fourth = input()
x = 0
one = first.replace(' ', '+')
two = second.replace(' ', '+')
three = third.replace(' ', '+')
four = fourth.replace(' ', '+')
one_split = first.split()
two_split = second.split()
three_split = third.split()
four_split = fourth.split()
answer = eval(one)
answer_two = eval(two)
answer_three = eval(three)
answer_four = eval(four)
if answer != answer_two or answer_three != answer_four or answer_two != answer_three:
    print('not magic')
else:
    for i in range(0, 4):
        vertical_one = int(one_split[i])
        vertical_two = int(two_split[i])
        vertical_three = int(three_split[i])
        vertical_four = int(four_split[i])
        equation = vertical_one + vertical_two + vertical_three + vertical_four
        if equation == answer:
            x += 1
        else:
            print('not magic')
            break

if x == 4:
    print('magic')
