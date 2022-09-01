import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([int(x) for x in input().split()])
print(sum([abs(arr[i] - arr[i + 1]) for i in range(0, 2 * n, 2)]))
