import sys
input = sys.stdin.readline


def findWord(a, b, w, ind):
    if w[ind] == "*":
        return 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if 0 <= a + i < n and 0 <= b + j < n and not visited[a + i][b + j] and w[ind] == grid[a + i][b + j]:
                visited[a + i][b + j] = 1
                if findWord(a + i, b + j, w, ind + 1):
                    return 1
                visited[a + i][b + j] = 0
    return 0


n, q = [int(x) for x in input().split()]
grid = [input().split() for _ in range(n)]
for _ in range(q):
    visited = [[0] * n for _ in range(n)]
    word = input()[:-1] + "*"
    done = 0
    for x in range(n):
        for y in range(n):
            if grid[x][y] == word[0]:
                visited[x][y] = 1
                if findWord(x, y, word, 1):
                    done = 1
                else:
                    visited[x][y] = 0
    if done:
        print("good puzzle!")
    else:
        print("bad puzzle!")
