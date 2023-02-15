from bisect import bisect_right
n, T = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
psa = [0] * n
for i in range(n):
    psa[i] = psa[i - 1] + arr[i]
m = 0
# print(psa)
for i in range(n):
    if psa[i] - arr[i] > T:
        break
    ind = bisect_right(psa, T + arr[i]) - 1
    # print(arr[i], ind)
    m = max(m, ind)
print(m)