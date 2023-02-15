def isValid(tmp):
    for x in tmp:
        if letters[x] not in want:
            return 0
    return 1


want = set([x for x in "ABCEGLOR"])
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    q, v, *swap = input().split()
    q = int(q)
    v = [letters.index(x) for x in v]
    original = v.copy()
    swap = [int(x) for x in swap]
    ct = 0
    solve = 1
    while not isValid(v):
        ct += 1
        for i in range(q):
            v[i] = (v[i] + swap[i]) % 26
        if v == original:
            solve = 0
            break
    if solve: print(ct)
    else: print('-1')
