n = int(input())
num = [0] * n
for _ in range(n):
    line = input()
    for i in range(n):
        if line[i] == "S":
            num[i] += 1
grid = [["."] * n for _ in range(n)]
for i in range(n):
    for j in range(num[i]):
        grid[-j-1][i] = "S"
[print("".join(i)) for i in grid]
