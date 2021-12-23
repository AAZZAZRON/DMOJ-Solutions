from sys import stdin
input = stdin.readline


cases = int(input())
for i in range(cases):
    lines = int(input())
    names = {}
    old = []
    for x in range(lines):
        name = input()[:-1]
        old.append(name)
        if name not in names:
            names[name] = 1
        else:
            names[name] += 1
    counter = 0
    max = 0
    add = True
    for name in old:
        names[name] -= 1
        if add:
            counter += 1
        else:
            counter -= 1
        add = False if names[name] == 0 else True
        if counter > max:
            max = counter
        # print(names, counter)
    print(len(old) * 10 - 20 * max)
