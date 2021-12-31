n = int(input())
arr = [int(input()) for _ in range(n)] + [0]
ct = 0
for i in range(n):
    if arr[i - 1] <= 41 and arr[i] <= 41 and arr[i + 1] <= 41:
        ct += 1
print(ct)