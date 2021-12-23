from sys import stdin
input = stdin.readline


def findWord(a, b, direction):
    word = ""
    counter = 0
    while 0 <= a < r and 0 <= b < c and grid[a][b] != "#":
        counter += 1
        word += grid[a][b]
        if direction == "horizontal":
            b += 1
        else:
            a += 1
    return "zzzzzzzzzzzzz" if counter <= 1 else word


r, c = [int(x) for x in input().split()]
grid = [input()[:-1] for _ in range(r)]
finalWord = "zzzzzzzzzzzzzzzzzzzz"
for x in range(r):
    for y in range(c):
        # vertical
        if x == 0 or grid[x - 1][y] == "#":
            finalWord = min(finalWord, findWord(x, y, "vertical"))
        # horizontal
        if y == 0 or grid[x][y - 1] == "#":
            finalWord = min(finalWord, findWord(x, y, "horizontal"))
print(finalWord)
