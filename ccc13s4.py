from sys import stdin
from collections import deque
input = stdin.readline


def isTaller(one, two):
    visited = [False] * (people + 1)
    visited[one] = True
    queue = deque([one])
    while queue:
        value = queue.popleft()
        for person in shorter[value]:
            if person == two:
                return True
            if not visited[person]:
                visited[person] = True
                queue.append(person)
    return False


people, lines = [int(x) for x in input().split()]
shorter = [[] for _ in range(people + 1)]
for _ in range(lines):
    x, y = [int(x) for x in input().split()]
    shorter[x].append(y)
a, b = [int(x) for x in input().split()]
if isTaller(a, b):
    print("yes")
elif isTaller(b, a):
    print("no")
else:
    print("unknown")
