import sys
input = sys.stdin.readline


numCases = int(input())
for i in range(numCases):
    string = input()
    toPrint = "YES"
    if string.count("(") == string.count(")"):
        open, close, find = 0, 0, 0
        for j in string:
            if j == "(":
                open += 1
            elif j == ")":
                close += 1
            if close > open:
                toPrint = "NO"
                break
    else:
        toPrint = "NO"
    print(toPrint)
