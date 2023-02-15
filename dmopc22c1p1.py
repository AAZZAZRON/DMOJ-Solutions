def upFirst(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] == 0 or arr[i] == 0:
            continue
        if i % 2 == 1 and arr[i] <= arr[i - 1]:
            return 0
        if i % 2 == 0 and arr[i] >= arr[i - 1]:
            return 0
    return 1


def downFirst(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] == 0 or arr[i] == 0:
            continue
        if i % 2 == 0 and arr[i] <= arr[i - 1]:
            return 0
        if i % 2 == 1 and arr[i] >= arr[i - 1]:
            return 0
    return 1


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print("YES" if upFirst(arr) or downFirst(arr) else "NO")