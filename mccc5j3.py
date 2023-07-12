n, k, m = map(int, input().split())
one = [int(x) for x in input().split()]
two = [int(x) for x in input().split()]
mapInd = {}
for i in range(n):
    mapInd[two[i]] = i
ct = 0
for i in range(n):
    v = one[i]
    want = m - v
    if want in mapInd and abs(mapInd[want] - i) >= k:
        ct += 1
print(ct)