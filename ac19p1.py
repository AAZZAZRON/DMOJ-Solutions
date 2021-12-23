import sys
input = sys.stdin.readline


cases = int(input())
for i in range(cases):
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    if N <= C:
        print(0, 0, N)
    elif N <= B + C:
        print(0, N - C, C)
    elif N > A + B + C:
        print(-1)
    else:
        print(N - C - B, B, C)
