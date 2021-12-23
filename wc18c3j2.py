import sys
input = sys.stdin.readline


num = int(input())
weight = [int(input()) for i in range(num)]
weight.append(101)
weight.sort()
weight = weight[:weight.index(101)]
if len(weight) >= 2:
    print(weight[-1] + weight[-2])
elif not weight:
    print(0)
else:
    print(weight[0])