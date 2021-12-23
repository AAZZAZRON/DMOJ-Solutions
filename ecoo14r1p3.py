from sys import stdin
input = stdin.readline


moves = [[1, 0], [0, 1], [1, 1], [-1, 1]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(5):
    r, c = [int(x) for x in input().split()]
    grid = [input()[:-1] for _ in range(r)]
    words = set()
    for _ in range(int(input())):
        before = input()[:-1]
        after = ""
        for i in before:
            if i in alphabet:
                after += i
        words.add(after)
    visited = set()
    for a in range(r):
        for b in range(c):
            for move in moves:
                path = set()
                word = ""
                x, y = a, b
                while True:
                    if 0 <= x < r and 0 <= y < c:
                        path.add((x, y))
                        word += grid[x][y]
                        if word in words or word[::-1] in words:
                            visited = visited.union(path)
                            break
                        x += move[0]
                        y += move[1]
                    else:
                        break
    sentence = ""
    for i in range(r):
        for j in range(c):
            if (i, j) not in visited:
                sentence += grid[i][j]
    print(sentence)
