disks = [1000, 500, 100, 50, 10, 5, 1]
arr = [0] * 7
n = int(input())
for i in range(7):
    arr[i] = n // disks[i]
    n %= disks[i]
print(" ".join([str(x) for x in arr[::-1]]))