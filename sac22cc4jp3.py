from math import atan2, degrees
n, A = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
tmp = degrees(atan2(b, a))
m = min((360 - abs(A - tmp)) % 360, abs(A - tmp) % 360)
ans = 1
for i in range(2, n + 1):
    a, b = [int(x) for x in input().split()]
    tmp = degrees(atan2(b, a))
    t = min((360 - abs(A - tmp)) % 360, abs(A - tmp) % 360)
    if t < m:
        m = t
        ans = i
print(ans)
