import sys
import heapq
input = sys.stdin.readline


n = int(input())
q = [[int(x) for x in input().split()] for _ in range(n)]
q.sort()
price = 0
arr = []
length = 0
for r in range(n, -1, -1):
    while q and q[-1][0] >= r:
        tmp = q.pop()
        heapq.heappush(arr, tmp[1])
        length += 1
    while length > n - r:
        price += heapq.heappop(arr)
        length -= 1
print(price)
