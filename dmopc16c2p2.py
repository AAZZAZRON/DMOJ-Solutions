import sys
from collections import deque
input = sys.stdin.readline


n, q = [int(x) for x in input().split()]
infected = [0] * (n + 1)
classInfected = [0] * (n + 1)
infected[1] = 1
queue = deque([1])
counter = 1
classes = []
connections = [[] for _ in range(n + 1)]
for i in range(q):
    tmp, *size = [int(x) for x in input().split()]
    classes.append(size)
    for j in size:
        connections[j].append(i)
while queue:
    node = queue.popleft()
    for next in connections[node]:
        if not classInfected[next]:
            classInfected[next] = 1
            for i in classes[next]:
                if not infected[i]:
                    infected[i] = 1
                    counter += 1
                    queue.append(i)
print(counter)
# print(infected)
print(" ".join([str(i) for i in range(1, n + 1) if infected[i]]))
