from sys import stdin
input = stdin.readline


rows = int(input())
col = int(input())
gold = 0
moves = int(input())
rowDict = {}
colDict = {}
for i in range(moves):
    move, num = input()[:-1].split()
    num = int(num)
    if move == "R":
        if num not in rowDict:
            rowDict[num] = 0
        rowDict[num] += 1
    elif move == "C":
        if num not in colDict:
            colDict[num] = 0
        colDict[num] += 1
for i in range(1, rows + 1):
    for j in range(1, col + 1):
        total = 0
        if i in rowDict:
            total += rowDict[i]
        if j in colDict:
            total += colDict[j]
        if total % 2 == 1:
            gold += 1
print(gold)
