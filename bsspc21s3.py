n, k = [int(x) for x in input().split()]
vals = [int(x) for x in input().split()]
curr, m = 0, 0
psa = [0] * (n + 1)
for i in range(1, n + 1):
    psa[i] = psa[i - 1] + vals[i - 1]
for i in range(k):
    curr = 0
    while i + k <= n:
        curr += psa[i + k] - psa[i]
        m = max(m, curr)
        if curr < 0:
            curr = 0
        i += k
print(m)
