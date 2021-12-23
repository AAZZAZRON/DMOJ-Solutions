n, q = [int(x) for x in input().split()]
cookies = [[0] * 501 for _ in range(501)]
grid = [[0] * 501 for _ in range(501)]
t = 0
for _ in range(q):
    cmd, *vals = [int(x) for x in input().split()]
    if cmd == 1:
        cookies[vals[0]][vals[1]] += 1
    else:
        for i in range(vals[0], vals[2] + 1):
            for j in range(vals[1], vals[3] + 1):
                t += cookies[i][j]
print(t)