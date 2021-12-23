from sys import stdin
input = stdin.readline


N, A, C = [int(x) for x in input().split()]
sweep = [[N + 1, 0, 0]]
for _ in range(A):
    a, b = [int(x) for x in input().split()]
    sweep.append([a, 1, 0])
    sweep.append([b + 1, -1, 0])
for _ in range(C):
    a, b = [int(x) for x in input().split()]
    sweep.append([a, 0, 1])
    sweep.append([b + 1, 0, -1])
sweep.sort()
counter = 0
anime, chores = 0, 0
for x in range(len(sweep) - 1):
    time, i, j = sweep[x]
    anime += i
    chores += j
    if sweep[x + 1][0] != time and chores == 0 and anime > 0:
        counter += sweep[x + 1][0] - time
print(counter)
