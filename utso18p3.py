import sys
from collections import deque
input = sys.stdin.readline


n, length, num, current = [int(x) for x in input().split()]
rest = [0] * (n + 1)
for _ in range(current):
    rest[int(input())] = 1
window = 0
empty = deque()
counter = 0
for i in range(1, length + 1):
    window += rest[i]
    if not rest[i]:
        empty.append(i)

while window < num:
    counter += 1
    window += 1
    rest[empty.pop()] = 1

for i in range(1, n - length + 1):
    window -= rest[i]
    window += rest[i + length]
    if empty and empty[0] == i:
        empty.popleft()
    if not rest[i + length]:
        empty.append(i + length)
    while window < num:
        counter += 1
        window += 1
        rest[empty.pop()] = 1
print(counter)
