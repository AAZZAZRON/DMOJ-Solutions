letters = {x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"}

for _ in range(5):
    line = input() + " "
    total = 0
    counter = 0
    for i in line:
        if i in letters:
            counter += 1
        else:
            if counter >= 4:
                total += 1
            counter = 0
    print(total)
