from sys import stdin
input = stdin.readline


def divide(x):
    number = [{x}]
    for i in range(numOps):
        added = set()
        queue = number.pop()
        for q in queue:
            if q < 0:
                continue
            for op in working:
                added.add(q - op)
                if q == 0 or op == 0:
                    continue
                if q % op == 0:
                    added.add(q // op)
        number.append(added)
    for j in working:
        if j in number[0]:
            return True
    return False


numOps = int(input())
numWorking = int(input())
working = [int(input()) for i in range(numWorking)]

for i in range(int(input())):
    num = int(input())
    if divide(num):
        print("Y")
    else:
        print("N")
