import sys
input = sys.stdin.readline


goBefore = {1: [2], 2: [], 3: [], 4: [1, 3], 5: [3], 6: [], 7: [1]}
count = []
while True:
    x = int(input())
    y = int(input())
    if x == y == 0:
        break
    goBefore[y].append(x)
while True:
    keys = list(goBefore.keys())
    values = list(goBefore.values())
    try:
        number = keys[values.index([])]
    except ValueError:
        if len(count) == 7:
            print(" ".join(count))
        else:
            print("Cannot complete these tasks. Going to bed.")
        break
    goBefore[number].append(0)
    count.append(str(number))
    for x in range(0, len(values)):
        i = values[x]
        if number in i:
            goBefore[x + 1].remove(number)
