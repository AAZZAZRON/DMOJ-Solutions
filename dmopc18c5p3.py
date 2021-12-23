n, v = [int(x) for x in input().split()]
longest = 0
s = 0
r = 0
arr = [int(x) for x in input().split()]
for l in range(n):
    while r < n and s + arr[r] < v:
        s += arr[r]
        r += 1
    if s < v:
        longest = max(longest, r - l)
    s -= arr[l]
print(longest)
