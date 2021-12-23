x = int(input())
one = input().split()
two = input().split()
numWar = 0
currentlyInWar = False
for i in range(0, x):
    if one[i] == two[i]:
        if not currentlyInWar:
            currentlyInWar = True
            numWar += 1
    else:
        if currentlyInWar:
            currentlyInWar = False
print(numWar)
