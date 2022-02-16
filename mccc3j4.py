from collections import deque


n, t = [int(x) for x in input().split()]
last = [int(x) - 1 for x in input().split()]
q = [deque([last[i]]) for i in range(n)]
for _ in range(t):
    used = [0] * n
    for i in range(n):
        if q[i]:
            used[i] = 1
    for i in range(n):
        if q[i] and used[i]:
            v = q[i].popleft()
            q[v].append(i)
            last[i] = v
print(" ".join([str(x + 1) for x in last]))
