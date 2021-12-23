num_spaces = int(input())
day_one = input()
day_two = input()
i = 0
amount = 0
while i < num_spaces:
    if day_one[i] == '.':
        i += 1
    else:
        if day_two[i] == 'C':
            amount += 1
            i += 1
        else:
            i += 1

print(str(amount))
