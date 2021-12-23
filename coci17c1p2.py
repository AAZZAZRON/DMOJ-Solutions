import sys
input = sys.stdin.readline


def search(a, b, letter):
    checked.append([a, b])
    visit.append([a, b])
    queue.append([a, b])
    while queue:
        a, b = queue.pop(0)
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != y and x != -y:
                    if x != 0 or y != 0:
                        if 0 <= a + x < gridX and 0 <= b + y < gridY:
                            if grid[a + x][b + y] == letter and [a + x, b + y] not in checked:
                                visit.append([a + x, b + y])
                                queue.append([a + x, b + y])
                                checked.append([a + x, b + y])


gridX, gridY = [int(num) for num in input().split()]
grid = [input() for i in range(gridX)]
checked = []
fig1, fig2, fig3, fig4, fig5 = 0, 0, 0, 0, 0
for i in range(gridX):
    for j in range(gridY):
        if grid[i][j] != "." and [i, j] not in checked:
            visit = []
            queue = []
            search(i, j, grid[i][j])
            visit.sort()
            x = [k[0] for k in visit]
            y = [k[1] for k in visit]
            if x[0] == x[1] == x[2] == x[3] and y[0] == y[1] - 1 == y[2] - 2 == y[3] - 3:
                fig2 += 1
            elif y[0] == y[1] == y[2] == y[3] and x[0] == x[1] - 1 == x[2] - 2 == x[3] - 3:
                fig2 += 1
            elif x[0] == x[1] == x[2] - 1 == x[3] - 1 and y[0] == y[1] - 1 == y[2] == y[3] - 1:
                fig1 += 1
            elif x[0] == x[1] == x[2] - 1 == x[3] - 1 and y[0] == y[1] - 1 == y[2] + 1 == y[3]:
                fig3 += 1
            elif x[0] == x[1] - 1 == x[2] - 1 == x[3] - 2 and y[0] == y[1] == y[2] - 1 == y[3] - 1:
                fig3 += 1
            elif x[0] == x[1] - 1 == x[2] - 1 == x[3] - 2 and y[0] == y[1] + 1 == y[2] == y[3] + 1:
                fig4 += 1
            elif x[0] == x[1] == x[2] - 1 == x[3] - 1 and y[0] == y[1] - 1 == y[2]-1 == y[3] - 2:
                fig4 += 1
            else:
                fig5 += 1
print(fig1)
print(fig2)
print(fig3)
print(fig4)
print(fig5)
