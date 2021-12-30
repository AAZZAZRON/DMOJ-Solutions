import sys
input = sys.stdin.readline


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


n, q = [int(x) for x in input().split()]
vals = [int(x) for x in input().split()]
lcm = [0] * (n + 1)
lcm[1] = vals[0]
for i in range(1, n):
    t = (lcm[i] * vals[i]) // gcd(lcm[i], vals[i])
    if t > 1000000000:
        for j in range(i + 1, n + 1):
            lcm[j] = 1000000000
        break
    lcm[i + 1] = t

# print(lcm)

for _ in range(q):
    v = int(input())
    if v == 0:
        print(-1)
        continue
    low, high = 1, n
    while high - low > 1:
        # print(low, high)
        mid = (low + high) // 2
        if lcm[mid] == 0 or v % lcm[mid] != 0:
            high = mid
        else:
            low = mid
    # print(low, high)
    if lcm[low] == 0 or v % lcm[low] != 0:
        print(low)
    elif lcm[high] == 0 or v % lcm[high] != 0:
        print(high)
    else:
        print(-1)
