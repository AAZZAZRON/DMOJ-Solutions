import sys
input = lambda: sys.stdin.readline()[:-1]


r, c = [int(x) for x in input().split()]
rows = [0] * r
col = [0] * c
for i in range(r):
    line = input()
    for j in range(c):
        if line[j] == "X":
            rows[i] = 1
            col[j] = 1
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    if rows[b - 1] or col[a - 1]:
        print("Y")
    else:
        print("N")
