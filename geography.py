import sys
input = sys.stdin.readline
arr = [1] * 100001
for i in range(2, 100001):
    for j in range(i, 100001, i):
        arr[j] += i * i

for _ in range(int(input())):
    print(arr[int(input())])
