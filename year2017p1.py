from collections import deque
import sys
input = lambda: sys.stdin.readline()[:-1]
nums = deque()
indexes = {}

for q in range(int(input())):
    cmd, n = input().split()
    if cmd == "F":
        nums.appendleft([n, q])
        indexes[n] = q
    elif cmd == "E":
        nums.append([n, q])
        indexes[n] = q
    else:
        indexes[n] = -1
for i, j in nums:
    if indexes[i] == j:
        print(i)


