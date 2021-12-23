import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    if n % k == 0:
        print(n // k)
    else:
        print(n // k + 1)
