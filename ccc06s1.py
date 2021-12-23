dad = input()
mom = input()
possible = set()
get = 0
for i in range(0, 10):
    possibility = [dad[i], mom[get]]
    possibility2 = [dad[i], mom[get + 1]]
    possible.add(sorted(possibility)[0])
    possible.add(sorted(possibility2)[0])
    if i % 2 == 1:
        get += 2
people = int(input())
for i in range(people):
    baby = input()
    isBaby = True
    for j in baby:
        if j not in possible:
            isBaby = False
            break
    if isBaby:
        print("Possible baby.")
    else:
        print("Not their baby!")
