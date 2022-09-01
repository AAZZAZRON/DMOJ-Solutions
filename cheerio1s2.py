import heapq
n, a, b = [int(x) for x in input().split()]
pq = [[a + b, 1, 1]]
heapq.heapify(pq)
tot = 0
for _ in range(n):
    cost, i, j = heapq.heappop(pq)
    tot += cost
    heapq.heappush(pq, [a * i + b * (j + 1), i, j + 1])
    if j == 1:
        heapq.heappush(pq, [a * (i + 1) + b, i + 1, 1])
print(tot)
