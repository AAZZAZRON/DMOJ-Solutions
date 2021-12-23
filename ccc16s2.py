solve = int(input())
numBikes = int(input())
side1 = sorted([int(x) for x in input().split()])
side2 = sorted([int(x) for x in input().split()])
sum = 0
for i in range(0, numBikes):
    if solve == 1:
        sum += max(side1[i], side2[i])
    else:
        sum += max(side1[i], side2[-(i + 1)])
print(sum)
