numPeople = int(input())
people = int(input())
infect = int(input())
total = people
day = 0
if infect == 1:
    print(numPeople // people)
elif people > numPeople:
    print(0)
else:
    while total <= numPeople:
        people *= infect
        total += people
        day += 1
    print(day)
