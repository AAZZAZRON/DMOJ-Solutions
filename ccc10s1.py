import sys
input = sys.stdin.readline


numComps = int(input())
if numComps == 1:
    print(input().split()[0])
else:
    first, second = ["", 0], ["", 0]
    for i in range(numComps):
        string = input().split()
        name, r, s, d = string[0], int(string[1]), int(string[2]), int(string[3])
        value = 2 * r + 3 * s + d
        if first[1] < value:
            second = first
            first = [name, value]
        elif second[1] < value:
            second = [name, value]
    if first[1] == second[1]:
        list = [first[0], second[0]]
        list.sort()
        print(list[0])
        print(list[1])
    else:
        print(first[0])
        print(second[0])
