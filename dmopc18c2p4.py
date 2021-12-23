n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
r = 0
s = 0
minimum = n + 1
for l in range(n):
    while r < n and s < m:
        s += arr[r]
        r += 1
    if s >= m:
        minimum = min(minimum, r - l)
    if r == n:
        break
    s -= arr[l]
if minimum == n + 1:
    print(-1)
else:
    print(minimum)
