from sys import stdin
input = stdin.readline


numBoxes = int(input())
boxes = [sorted(int(x) for x in input().split()) for i in range(numBoxes)]
# print(boxes)
numItems = int(input())
for i in range(numItems):
    fail = True
    item = sorted(int(x) for x in input().split())
    volume = 2000 * 2000 * 2000 + 1
    for j in boxes:
        if item[0] <= j[0] and item[1] <= j[1] and item[2] <= j[2]:
            fail = False
            volume = min(j[0] * j[1] * j[2], volume)
    if fail:
        print("Item does not fit.")
    else:
        print(volume)
