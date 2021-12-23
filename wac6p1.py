import sys
input = sys.stdin.readline


numCases = int(input())
for i in range(numCases):
    P, C = [float(x) for x in input().split()]
    originalPrice = 100 * P / (C + 100)
    originalPrice = int(originalPrice * 1000000000 + 0.5) / 1000000000
    print(originalPrice)
