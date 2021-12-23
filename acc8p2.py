import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    line = [int(x) for x in input().split()]
    counter = 0
    total = 0
    for i in line:
        total += i
        if total >= k:
            counter += 1
            total = 0
    print(counter)
