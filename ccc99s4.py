from sys import stdin
input = stdin.readline


num = int(input())
kM = [[2, 1], [1, 2], [-1, 2], [2, -1], [-2, 1], [1, -2], [-1, -2], [-2, -1]]
for i in range(num):
    rows, col, a, b, c, d = [int(input()) for q in range(6)]
    pawn = [a, b]
    knight = (c, d)
    queue = [[knight]]
    counter = 0
    hasStale, hasWon = False, False
    wC, sC = 0, 0
    added = {knight}
    while queue and pawn[0] != rows and not hasWon:
        if tuple(pawn) in added:
            hasWon = True
            wC = counter
        pawn[0] += 1
        if tuple(pawn) in added and not hasStale:
            hasStale = True
            sC = counter
        added = set()
        queued = queue.pop()
        for x, y in queued:
            for a, b in kM:
                a += x
                b += y
                if 0 < a <= rows and 0 < b <= col:
                    added.add((a, b))
        counter += 1
        if added:
            queue.append(added)

    if hasWon:
        print(f"Win in {wC} knight move(s).")
    elif hasStale:
        print(f"Stalemate in {sC} knight move(s).")
    else:
        print(f"Loss in {rows - (pawn[0] - counter) - 1} knight move(s).")
