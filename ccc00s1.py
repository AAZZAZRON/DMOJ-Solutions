money = int(input())
oneCount = int(input())
twoCount = int(input())
threeCount = int(input())
plays = 0
while True:
    oneCount += 1
    plays += 1
    money -= 1
    if money <= 0:
        break
    if oneCount == 35:
        money += 30
        oneCount = 0
    twoCount += 1
    plays += 1
    money -= 1
    if money <= 0:
        break
    if twoCount == 100:
        money += 60
        twoCount = 0
    threeCount += 1
    plays += 1
    money -= 1
    if money <= 0:
        break
    if threeCount == 10:
        money += 9
        threeCount = 0
print("Martha plays {} times before going broke.".format(plays))
