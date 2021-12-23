import sys
from collections import deque
input = sys.stdin.readline


def solve(left, right, queue):
    while queue:
        if queue[0] + 1 == left:
            left = queue.popleft()
        elif queue[0] - 1 == right:
            right = queue.popleft()
        elif queue[-1] + 1 == left:
            left = queue.pop()
        elif queue[-1] - 1 == right:
            right = queue.pop()
        else:
            return 0
    return 1


for c in range(int(input())):
    n = int(input())
    q = deque()
    for i in [int(x) for x in input().split()]:
        q.append(i)
    tmp = q.popleft()
    solved = solve(tmp, tmp, q.copy())
    q.appendleft(tmp)

    tmp = q.pop()
    solved = max(solved, solve(tmp, tmp, q))
    if solved:
        print(f"Case #{c + 1}: yes")
    else:
        print(f"Case #{c + 1}: no")
