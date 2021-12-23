def testRoad(road, noGo, letter, key):
    if letter == key:
        if "!" not in sus:
            sus.append("!")
        return
    valid.add(letter)
    for i in road[letter]:
        if i != noGo and i not in valid:
            testRoad(road, noGo, i, key)


def testRoad2(road, noGo, noGo2, letter):
    if letter == "B":
        if "!" not in finalSus:
            finalSus.append("!")
        return
    valid.add(letter)
    for i in road[letter]:
        if i not in valid:
            if i == noGo and letter == noGo2:
                pass
            elif i == noGo2 and letter == noGo:
                pass
            else:
                testRoad2(road, noGo, noGo2, i)


valid = set()
inputs = []
roads = {}
sus = []
finalSus = []
while True:
    x = input()
    if x == "**":
        break
    inputs.append(x)
    one = x[0]
    two = x[1]
    if one not in roads:
        roads[one] = [two]
    else:
        roads[one].append(two)
    if two not in roads:
        roads[two] = [one]
    else:
        roads[two].append(one)
for i in roads.keys():
    valid = set()
    if i != "A":
        testRoad(roads, i, "A", "B")
    else:
        testRoad(roads, "A", "B", "A")
    if sus.count("!") == 1:
        del sus[-1]
    else:
        sus.append(i)
counter = 0
for i in sus:
    for j in sus:
        if i != j and j + i not in finalSus:
            valid = set()
            testRoad2(roads, i, j, "A")
            if finalSus.count("!") == 1:
                del finalSus[-1]
            else:
                finalSus.append(i + j)
for i in finalSus:
    print(i)
    counter += 1
print("There are {} disconnecting roads.".format(counter))
