import sys
input = sys.stdin.readline

n, s = [int(x) for x in input().split()]
g = n // s
groups = [[int(x) for x in input().split()] for _ in range(g)]

score = [0] * 2001
for _ in range((s - 1) * n // 2):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    if c == "W":
        score[a] += 3
    elif c == "L":
        score[b] += 3
    else:
        score[a] += 1
        score[b] += 1
k = int(input())
for i in range(g):
    print(-sorted([[score[x], -x] for x in groups[i]], reverse=True)[k - 1][1], end=" " if i + 1 != g else "\n")
