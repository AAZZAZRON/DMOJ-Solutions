n, k = [int(x) for x in input().split()]
arr = sorted([int(x) for x in input().split()])
if n < k:
    print(arr[-1])
else:
    d = arr[k - 1]
    inf = k
    l = k
    r = n
    while l < r and arr[l] == d:
        l += 1
        inf += 1
    while l < r:
        d += 1
        r -= inf // k
        inf += inf // k
        while l < r and arr[l] == d:
            l += 1
            inf += 1
    print(d)