def recurse(val):
    global ans
    while arr[val]:
        recurse(arr[val][-1])
        arr[val].pop()
    if not prereq[val]:
        ans.append(val)
        prereq[val] = 1


import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input())
arr = [[] for _ in range(n + 1)]
ans = []
prereq = [0] * (n + 1)
for i in range(n):
    _, *pre = [int(x) for x in input().split()]
    arr[i + 1] = pre
for i in range(1, n + 1):
    recurse(i)
print(*ans)