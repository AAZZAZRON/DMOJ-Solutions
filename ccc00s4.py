import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline


def golfing(number, counter=0, memo=None):
    global lowest
    if memo is None:
        memo = {}
    if number == 0:
        if lowest > counter:
            lowest = counter
        return counter
    if number in memo:
        return memo[number]
    memo[number] = 0
    for i in possible:
        if number - i >= 0:
            memo[number] -= counter
            memo[number] += golfing(number - i, counter + 1, memo)
    return memo[number]


getTo = int(input())
numMoves = int(input())
possible = [int(input()) for i in range(numMoves)]
possible.sort()
possible.reverse()
lowest = 5281
golfing(getTo)
if lowest == 5281:
    print("Roberta acknowledges defeat.")
else:
    print(f"Roberta wins in {lowest} strokes.")
