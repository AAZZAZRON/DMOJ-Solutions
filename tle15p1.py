import sys
input = sys.stdin.readline


n, q = [int(x) for x in input().split()]
names = [input()[:-1] for _ in range(n)]
values = [[0, i] for i in range(n)]
for _ in range(q):
    line = [int(x) for x in input().split()]
    for i in range(n):
        values[i][0] += line[i]
values.sort(reverse=True)
for i in range(n):
    print(f"{i + 3}. {names[values[i][1]]}")
