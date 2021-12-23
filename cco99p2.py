import sys
input = sys.stdin.readline


times = int(input())
for i in range(times):
    words = {}
    lines, place = [int(x) for x in input().split()]
    for j in range(lines):
        x = input()[:-1]
        if x in words:
            words[x] += 1
        else:
            words[x] = 1
    if place % 100 != 11 and place % 10 == 1:
        number = f"{place}st"
    elif place % 100 != 12 and place % 10 == 2:
        number = f"{place}nd"
    elif place % 100 != 13 and place % 10 == 3:
        number = f"{place}rd"
    else:
        number = f"{place}th"
    print(f"{number} most common word(s):")
    ranks = list(set(sorted(words.values())))
    values = list(words.values())
    ind = 0
    q = 1
    if place == 1:
        go = False
        q = 2
    else:
        go = True
    while ind < place != 1 and q <= len(ranks):
        ind += values.count(ranks[-q])
        q += 1
        if ind > place:
            go = False
    if go:
        continue
    index = ranks[-q + 1]
    for key in words:
        if words[key] == index:
            print(key)
