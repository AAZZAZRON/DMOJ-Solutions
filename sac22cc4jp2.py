n, q = [int(x) for x in input().split()]
arr = [0] * (n + 1)
s = {"square": 1, "circle": 2, "triangle": 3}
for _ in range(q):
    g, shape, ind = input().split()
    ind = int(ind)
    if g == "get":
        print(1 if arr[ind] == s[shape] else 0)
    else:
        arr[ind] = s[shape]
