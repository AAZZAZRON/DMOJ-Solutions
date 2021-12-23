import sys
input = sys.stdin.readline


m = int(input())
hasClass = [0] * 1441
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    for i in range(a, b + 1):
        hasClass[i] = 1
n = int(input())
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    found = 0
    for i in range(a, b + 1):
        if hasClass[i]:
            found = 1
            break
    if found:
        print("Break is Over! Stop playing games! Stop watching Youtube!")
    else:
        print(":eyy:")
