def findWord(grid, word, x, y, goX, goY, letter):
    if grid[x][y].lower() == word[letter].lower():
        if letter + 1 == len(word):
            found.append("FOUND")
            return
        if 0 <= x + goX <= m - 1 and 0 <= y + goY <= n - 1:
            return findWord(grid, word, x + goX, y + goY, goX, goY, letter + 1)
    else:
        return


numCases = int(input())
for i in range(0, numCases):
    x = input()
    xSplit = x.split()
    m = int(xSplit[0])
    n = int(xSplit[1])
    grid = []
    for j in range(0, m):
        x = input()
        list = []
        for k in x:
            list.append(k)
        grid.append(list)
    numTest = int(input())
    for j in range(0, numTest):
        word = input()
        possible = []
        for x in range(0, m):
            for y in range(0, n):
                found = []
                if grid[x][y].lower() != word[0].lower():
                    continue
                for goX in range(-1, 2):
                    for goY in range(-1, 2):
                        if goX == 0 and goY == 0:
                            continue
                        findWord(grid, word, x, y, goX, goY, 0)
                        if "FOUND" in found:
                            possible.append([x + 1, y + 1])
                            break
                    if "FOUND" in found:
                        break
        possible.sort()
        print(possible[0][0], possible[0][1])
