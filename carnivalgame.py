import sys
input = lambda: sys.stdin.readline()[:-1]

n = int(input())
dp = []
for i in range(1, n):
    dp.append([-1000000001] * i)
lines = [input() for _ in range(n - 1)]
dp.append([int(x) for x in input().split()])
for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        dp[i][j] = dp[i + 1][j] - (lines[i][j] != "L")
        dp[i][j] = max(dp[i][j], dp[i + 1][j + 1] - (lines[i][j] != "R"))
print(dp[0][0])
j = 0
f = []
for i in range(n - 1):
    flip = 0
    addJ = 0
    if dp[i + 1][j] == dp[i][j] == dp[i + 1][j + 1]:
        if lines[i][j] == "R":
            addJ = 1
    elif dp[i + 1][j] == dp[i][j]:
        pass
    elif dp[i + 1][j + 1] == dp[i][j]:
        addJ = 1
    elif dp[i + 1][j] == dp[i][j] + 1:
        flip = 1
    elif dp[i + 1][j + 1] == dp[i][j] + 1:
        flip = 1
        addJ = 1
    if flip:
        f.append(f"{i + 1} {j + 1}")
    if addJ:
        j += 1
print(len(f))
[print(x) for x in f]
