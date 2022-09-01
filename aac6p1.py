n, k = [int(x) for x in input().split()]
arr = [x for x in range(1, n + 1)]
s = (n * (n + 1) // 2) % k
arr[-1] += k - s
print(*arr)