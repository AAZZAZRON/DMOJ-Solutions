import heapq
import sys
input = sys.stdin.readline


moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for _ in range(5):
    r, c = [int(x) for x in input().split()]
    pq = []
    grid = []
    visited = [[0] * c for _ in range(r)]
    for i in range(r):
        line = [int(x) for x in input().split()]
        if i == 0 or i == r - 1:
            for j in range(c):
                visited[i][j] = 1
                pq.append([line[j], i, j])
        else:
            visited[i][0] = visited[i][-1] = 1
            pq.append([line[0], i, 0])
            pq.append([line[-1], i, c - 1])
        grid.append(line)
    pq.sort()
    heapq.heapify(pq)
    # print(pq)
    count = 0
    maximum = 0
    while pq:
        n, a, b = heapq.heappop(pq)
        maximum = max(maximum, n)
        for x, y in moves:
            x += a
            y += b
            if 0 <= x < r and 0 <= y < c and not visited[x][y]:
                visited[x][y] = 1
                if grid[x][y] < maximum:
                    count += maximum - grid[x][y]
                heapq.heappush(pq, [grid[x][y], x, y])
    print(count)
