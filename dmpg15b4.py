from sys import stdin
input = stdin.readline


num = int(input())
numbers = [int(input()) for _ in range(num)]
maximum = 1
negatives = []
hasZero = False
for x in numbers:
    if x > 0:
        maximum *= x
    elif x < 0:
        negatives.append(x)
    else:
        hasZero = True
if len(negatives) == 0:
    pass
elif len(negatives) % 2 == 0:
    for x in negatives:
        maximum *= x
else:
    negatives.sort()
    for x in negatives[:-1]:
        maximum *= x
if maximum == 1 and 1 not in numbers:
    if hasZero:
        maximum = 0
    elif len(negatives) == 1:
        maximum = negatives[0]
print(maximum)
