from sys import stdin
from collections import deque
input = stdin.readline


for _ in range(5):
    num = int(input())
    routes = {}
    queue = deque([["YYZ", 0]])
    visited = {"YYZ"}
    minimum = 99999999999999
    for _ in range(num):
        a, b, c = input()[:-1].split()
        if a not in routes:
            routes[a] = []
        routes[a].append([b, int(c)])

    while queue:
        dest, price = queue.popleft()
        if dest in routes:
            for a, b in routes[dest]:
                if a == "SEA":
                    minimum = min(minimum, b + price)
                elif a not in visited:
                    visited.add(a)
                    queue.append([a, price + b])
    print(minimum)
