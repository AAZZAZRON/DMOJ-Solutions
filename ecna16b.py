from collections import deque


n = int(input())
people = input().split()
score = input()
score += "B" if score[-1] == "W" else "W"
maximum = 0
dynasties = []
before = ""
current = -1
wO, bO, wD, bD = people[:4]
off = deque(people[4:])
lose = []
for i in score:
    if i == "B":
        bO, bD = bD, bO
    else:
        wO, wD = wD, wO
    if i != before:
        if maximum == 0:
            lose = lose[::-1]
        if current > maximum:
            maximum = current
            dynasties = [lose]
        elif current == maximum:
            dynasties.append(lose)
        if i == "W":
            lose = [wO, wD]
        else:
            lose = [bO, bD]
        current = 1
    else:
        current += 1
    if i == "W":
        off.append(bD)
        bD = bO
        bO = off.popleft()
    else:
        off.append(wD)
        wD = wO
        wO = off.popleft()
    before = i
[print(x, y) for x, y in dynasties]
