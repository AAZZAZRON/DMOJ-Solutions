import sys
from collections import deque
input = sys.stdin.readline

cars = deque()
q, m = [int(x) for x in input().split()]
for _ in range(q):
    name, cmd = input().split()
    if cmd == "in":
        cars.append(name)
    elif cars[-1] == name:
        cars.pop()
    elif cars[0] == name and m >= 1:
        m -= 1
        cars.popleft()
[print(x) for x in cars]
