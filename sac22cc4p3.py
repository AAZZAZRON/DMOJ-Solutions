n = int(input())
arr = sorted([int(x) for x in input().split()])
if n % 2 == 1:
    print(arr[n // 2])
else:
    print((arr[n // 2 - 1] + arr[n // 2]) // 2)