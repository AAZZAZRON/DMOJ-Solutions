from bisect import bisect_left
arr = [0, 1]
while arr[-1] <= 10 ** 10:
    arr.append(arr[-2] + arr[-1])
for _ in range(5):
    n = int(input())
    ind = bisect_left(arr, n)
    d = n - arr[ind - 1]
    d2 = arr[ind] - n
    if d < d2:
        print(arr[ind - 1])
    else:
        print(arr[ind])
