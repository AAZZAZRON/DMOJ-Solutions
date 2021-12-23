import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input()) for _ in range(n)])
right = n - 1
total = 0
for left in range(n):
    total += arr[left] * arr[right]
    right -= 1
print(total % 10007)
