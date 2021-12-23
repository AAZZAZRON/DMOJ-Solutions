from sys import stdin
input = stdin.readline


num = int(input())
if num == 2:
    print(1, 1)
else:
    list = []
    firstLine = [int(x) for x in input().split()]
    second = [int(x) for x in input().split()][2]
    a = firstLine[1]
    a -= second
    a += firstLine[2]
    a //= 2
    for i in firstLine:
        if i == 0:
            list.append(str(a))
        else:
            list.append(str(i - a))
    print(" ".join(list))
