from sys import stdin
from collections import deque
input = stdin.readline


numCities = int(input())
numRoutes = int(input())
queue = deque()
routes = [[999999999] * (numCities + 1) for _ in range(numCities + 1)]
minimum = [9999999999999] * (numCities + 1)
for i in range(numRoutes):
    one, two, cost = [int(x) for x in input().split()]
    routes[one][two] = min(routes[one][two], cost)
    routes[two][one] = min(routes[two][one], cost)
sellers = int(input())
for i in range(sellers):
    a, b = [int(x) for x in input().split()]
    minimum[a] = b
    queue.append([a, b])

lookingFor = int(input())
while queue:
    node, cost = queue.popleft()
    for next in range(1, numCities + 1):
        added = routes[node][next]
        if cost + added < minimum[next]:
            minimum[next] = cost + added
            queue.append([next, cost + added])
print(minimum[lookingFor])
