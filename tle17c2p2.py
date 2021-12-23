import sys
inpunt = sys.stdin.readline


n = int(input())
numbers = set([int(x) for x in input().split()])
val = [0] * 1000001
for i in range(1000001):
    if i in numbers:
        val[i] = val[i - 1] + 1
    else:
        val[i] = val[i - 1]
for _ in range(int(input())):
    x = int(input())
    print(x - val[x])
