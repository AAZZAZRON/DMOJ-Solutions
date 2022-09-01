def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
arr = [int(x) for x in input().split()]
g = arr[0]
for i in range(1, n):
    g = gcd(g, arr[i])
print(*[x // g for x in arr])
