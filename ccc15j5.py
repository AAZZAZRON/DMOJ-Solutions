def findCombos(pie, before, people, memo=None, counter=0):
    if memo is None:
        memo = {}
    global count
    if people == 1:
        count += 1
        return 1
    elif (people, before, pie) in memo:
        count += memo[(people, before, pie)]
        return memo[(people, before, pie)]
    for i in range(before, pie // people + 1):
        counter += findCombos(pie - i, i, people - 1, memo)
    memo[(people, before, pie)] = counter
    return counter


numPi = int(input())
numPeople = int(input())
count = 0
findCombos(numPi, 1, numPeople)
print(count)
