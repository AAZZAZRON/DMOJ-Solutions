from sys import stdin, exit
input = stdin.readline


conversions = {}
num, lines = [int(x) for x in input().split()]

lookingFor = set()
minimum, routes = {"English": [0, 0]}, {"English": []}
for i in input().split():
    lookingFor.add(i)
    minimum[i] = [99999999, 99999999]
    routes[i] = []

for _ in range(lines):
    x, y, cost = input().split()
    routes[x].append([y, int(cost)])
    routes[y].append([x, int(cost)])
queue = [[["English", 0]]]
counter = 0
while queue:
    counter += 1
    queued = queue.pop()
    addArr = []
    for lang, cost in queued:
        for ling, added in routes[lang]:
            if counter < minimum[ling][1]:
                minimum[ling] = [added + cost, counter]
                if ling in lookingFor:
                    addArr.append([ling, 0])
                else:
                    addArr.append([ling, added + cost])
            elif counter == minimum[ling][1] and added + cost < minimum[ling][0]:
                minimum[ling] = [added + cost, counter]
                if ling in lookingFor:
                    addArr.append([ling, 0])
                else:
                    addArr.append([ling, added + cost])
    if addArr:
        queue.append(addArr)
total = 0
for i, j in minimum.values():
    if i == 99999999:
        print("Impossible")
        exit()
    total += i
print(total)
