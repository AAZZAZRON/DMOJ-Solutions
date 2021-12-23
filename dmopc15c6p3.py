n, m, k = [int(x) for x in input().split()]
diff = [0] * (n + 1)
for _ in range(m):
    a, b = [int(x) - 1 for x in input().split()]
    diff[a] += 1
    diff[b + 1] -= 1
potatos = [m] * n
diff[-1] = 0
for i in range(n):
    diff[i] += diff[i - 1]
    potatos[i] -= diff[i]
r = 0
s = 0
minimum = n + 1
for l in range(n):
    while r < n and s < k:
        s += potatos[r]
        r += 1
    if s >= k:
        minimum = min(minimum, r - l)
    s -= potatos[l]
if minimum == n + 1:
    print(-1)
else:
    print(minimum)
