import sys
input = lambda: sys.stdin.readline()[:-1]


def check(a, b, one, two):
    number = psa[a + one][b + two] - psa[a][b + two] - psa[a + one][b] + psa[a][b]
    return number == 0


n, m = [int(x) for x in input().split()]
ySize, xSize = [int(x) for x in input().split()]
psa = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    line = input()
    for j in range(1, m + 1):
        v = line[j - 1] == "#"
        psa[i][j] = psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + v
# [print(x) for x in psa]
moves = ((1, 0), (-1, 0), (0, -1), (0, 1))
bottom, right = n - ySize, m - xSize
if check(0, 0, ySize, xSize):
    queue = [[[0, 0]]]
else:
    print(-1)
    sys.exit()
visited = [[0] * m for _ in range(n)]
counter = 0
visited[0][0] = 1
while queue:
    counter += 1
    queued = queue.pop()
    added = []
    for a, b in queued:
        if a == bottom and b == right:
            print(counter - 1)
            sys.exit()
        for x, y in moves:
            x += a
            y += b
            if 0 <= x <= bottom and 0 <= y <= right and not visited[x][y] and check(x, y, ySize, xSize):
                visited[x][y] = 1
                added.append([x, y])
    if added:
        queue.append(added)
print(-1)
