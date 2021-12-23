numLights = int(input())
original = input()
goTo = set()
start = False
tmp = 0
for x in range(numLights):
    if original[x] == "0" and not start:
        tmp = x
        start = True
    elif original[x] == "1" and start:
        goTo.add((tmp, x - 1))
        start = False
if start:
    goTo.add((tmp, numLights - 1))
counter = 0
for start, end in goTo:
    value = abs(start - end) + 1
    if start == 0 or end == numLights - 1:
        counter += (value * (value + 1) // 2)
    else:
        height = (value + 1) // 2
        counter += 2 * (height * (height + 1) // 2)
        if value % 2 == 1:
            counter -= height
print(counter)
