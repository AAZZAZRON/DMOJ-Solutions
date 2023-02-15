n = int(input())
h = [int(x) for x in input().split()]
ct = 1
curr = 1
for i in range(1, n):
    if h[i - 1] >= h[i]:
        ct = max(ct, curr)
        curr = 0
    curr += 1
ct = max(ct, curr)

print(ct)
ct = 1
curr = 1
for i in range(1, n):
    if h[i - 1] <= h[i]:
        ct = max(ct, curr)
        curr = 0
    curr += 1
ct = max(ct, curr)
print(ct)