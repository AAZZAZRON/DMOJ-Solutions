time = int(input())
start_h = 0
start_m = 0
amount = 0
if time >= 720:
    extra = int(time/720)
    amount = 31 * extra
    time = time % 720
if time >= 60:
    extra = int(time / 60)
    start_h = extra
    start_m = time % 60
else:
    start_m = time
for i in range(0, start_h):
    if i == 0:
        i = 12
    if i == 10 or i == 11 or i == 12:
        i = str(i)
        i = i[0] + ' ' + i[1] + ' '
    else:
        i = str(i)
        i = i + ' '
    for j in range(0, 60):
        if j < 10:
            j = '0 ' + str(j)
        else:
            j = str(j)
            j = j[0] + ' ' + j[1]
        num = i + j
        num_split = num.split()
        if len(num_split) == 3 and int(num_split[2]) - int(num_split[1]) == int(num_split[1]) - int(num_split[0]):
            amount += 1
        elif len(num_split) == 4 and int(num_split[3]) - int(num_split[2]) == int(num_split[2]) - int(num_split[1]) and int(num_split[2]) - int(num_split[1]) == int(num_split[1]) - int(num_split[0]):
            amount += 1

i = start_h
if i == 0:
    i = 12
if i == 10 or i == 11 or i == 12:
    i = str(i)
    i = i[0] + ' ' + i[1] + ' '
else:
    i = str(i)
    i = i + ' '
for j in range(0, start_m + 1):
    if j < 10:
        j = '0 ' + str(j)
    else:
        j = str(j)
        j = j[0] + ' ' + j[1]
    num = i + j
    num_split = num.split()
    if len(num_split) == 3 and int(num_split[2]) - int(num_split[1]) == int(num_split[1]) - int(num_split[0]):
        amount += 1
    elif len(num_split) == 4 and int(num_split[3]) - int(num_split[2]) == int(num_split[2]) - int(num_split[1]) and int(num_split[2]) - int(num_split[1]) == int(num_split[1]) - int(num_split[0]):
        amount += 1
print(amount)
