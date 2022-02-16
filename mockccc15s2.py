n = int(input())
arr = [0] * 100001
for i in [int(x) for x in input().split()]:
    arr[i] += 1
print(max(arr))
