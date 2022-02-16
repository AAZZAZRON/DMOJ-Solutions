import sys
n = int(input())
arr = [int(x) for x in input().split()]
tot = sum(arr)
curr = 0
for i in range(n):
    curr += arr[i]
    tot -= arr[i]
    if curr == tot:
        print(i + 1)
        sys.exit()
print("Andrew is sad.")