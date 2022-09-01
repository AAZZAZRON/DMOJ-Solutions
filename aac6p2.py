n, q = [int(x) for x in input().split()]
m = 1
start = [0] * (n + 1)
end = [0] * (n + 1)
for _ in range(q):
    a, b = [int(x) for x in input().split()]
    m = max(m, b - a + 1)
    start[a - 1] += 1
    end[b] += 1

arr = [1] * n
ct = 0
for i in range(n):
    if ct == 0 or ct - end[i] == 0:
        arr[i] = arr[i - 1]
    else:
        arr[i] = (arr[i - 1]) % m + 1
    ct -= end[i]
    ct += start[i]

print(m)
print(*arr)
