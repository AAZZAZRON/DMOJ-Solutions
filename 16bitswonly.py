import sys
input = sys.stdin.readline


times = int(input())
for i in range(times):
    x = input().split()
    if int(x[0]) * int(x[1]) == int(x[2]):
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")
