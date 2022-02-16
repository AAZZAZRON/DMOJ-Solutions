v = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
s = sum(v)
n = int(input())
for _ in range(n):
    s -= v[int(input()) - 1]
s /= (10 - n)
if int(input()) > s:
    print("deal")
else:
    print("no deal")