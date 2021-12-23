num = int(input())
for i in range(0, num):
    x = int(input())
    factorsList = []
    solution = 0
    for j in range(1, x):
        factor = j
        if x % factor == 0:
            factorsList.append(factor)
    for j in range(0, len(factorsList)):
        solution += factorsList[j]

    if solution == x:
        print(str(x) + " is a perfect number.")
    elif solution > x:
        print(str(x) + " is an abundant number.")
    elif solution < x:
        print(str(x) + " is a deficient number.")
