import sys
input = sys.stdin.readline


numProblems = int(input())
cutenessFactor = [int(x) for x in input().split()]
time = 0
problem = []
for i in range(numProblems):
    inputs = [int(x) for x in input().split()]
    if inputs[2] > time:
        time = inputs[2]
    problem.append(inputs)
while problem:
    solving = problem.pop(0)
    if solving[1] != 10:
        cuteness = cutenessFactor[solving[0] - 1]
        timeToSolve = cuteness * solving[3]
        if time + timeToSolve <= 180:
            print(10 - solving[1])
        else:
            print("The kemonomimi are too cute!")
    else:
        print(0)
