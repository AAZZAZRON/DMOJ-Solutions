import sys
from collections import deque
input = sys.stdin.readline


def check(a, b, size):
    return 0 == psa[a + size - 1][b + size - 1] - psa[a - 1][b + size - 1] - psa[a + size - 1][b - 1] + psa[a - 1][b - 1]


moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, m = [int(x) for x in input().split()]
psa = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    line = input()[:-1]
    for j in range(1, m + 1):
        v = line[j - 1] == "X"
        psa[i][j] = psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + v

low, high = 1, 0
while high < min(n, m) and check(1, 1, high + 1):
    high += 1

while low <= high:
    size = (low + high) // 2
    queue = deque([[1, 1]])
    visited = [0] * ((n + 1) * (m + 1))
    visited[m + 2] = 1
    bottom, right = n - size + 1, m - size + 1
    while queue:
        a, b = queue.popleft()
        if a == bottom and b == right:
            low = size + 1
            break
        for x, y in moves:
            x = x + a
            y = y + b
            if 1 <= x <= bottom and 1 <= y <= right and not visited[x * (m + 1) + y] and check(x, y, size):
                visited[x * (m + 1) + y] = 1
                queue.append([x, y])
    else:
        high = size - 1
print(high)
