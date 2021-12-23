import sys
input = sys.stdin.readline


def solve():
    noBosses = people.difference(whoHasBosses)
    if len(noBosses) == 1 and not isInvalid:
        print(noBosses.pop())
    else:
        print("INVALID")
    return


whoHasBosses = set()
people = set()
isInvalid = False
while True:
    line = [int(x) for x in input().split()]
    for i in range(0, len(line), 2):
        j = i + 1
        if line[i] == line[j] == 0:
            solve()
            whoHasBosses = set()
            people = set()
            isInvalid = False
        elif line[i] == line[j] == -1:
            sys.exit()
        else:
            people.add(line[i])
            people.add(line[j])
            if line[j] in whoHasBosses:
                isInvalid = True
            whoHasBosses.add(line[j])
