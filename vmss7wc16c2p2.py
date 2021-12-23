from sys import stdin
input = stdin.readline


string = input()
psa = [0]
numG = 0
for i in string:
    if i == "G":
        numG += 1
    psa.append(numG)
num = int(input())
for i in range(num):
    x, y = [int(x) for x in input().split()]
    print(psa[y + 1] - psa[x])
