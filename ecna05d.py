from sys import stdin
input = stdin.readline


kM = [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]
num = 1
while True:
    rows, col = [int(x) for x in input().split()]
    if rows == col == 0:
        break
    safe = rows * col
    num1, *queens = [int(x) for x in input().split()]
    num2, *knights = [int(x) for x in input().split()]
    num3, *pawns = [int(x) for x in input().split()]

    # get the piece places
    pieces = set()
    [pieces.add((queens[x], queens[x + 1])) for x in range(0, num1 * 2, 2)]
    [pieces.add((knights[x], knights[x + 1])) for x in range(0, num2 * 2, 2)]
    [pieces.add((pawns[x], pawns[x + 1])) for x in range(0, num3 * 2, 2)]

    visited = set()
    # queen moves
    for x in range(0, num1 * 2, 2):
        for i in range(-1, 2):
            for j in range(-1, 2):
                m = i + queens[x]
                n = j + queens[x + 1]
                while 0 < m <= rows and 0 < n <= col:
                    if (m, n) in pieces:
                        break
                    visited.add((m, n))
                    m += i
                    n += j

    # knight moves
    for x in range(0, num2 * 2, 2):
        for i, j in kM:
            m = i + knights[x]
            n = j + knights[x + 1]
            if 0 < m <= rows and 0 < n <= col:
                visited.add((m, n))

    print(f"Board {num} has {safe - len(visited.union(pieces))} safe squares.")
    num += 1
