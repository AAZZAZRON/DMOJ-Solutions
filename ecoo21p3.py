from sys import stdin
input = stdin.readline


num, profs, q = [int(x) for x in input().split()]
final = [-1] * num
maxScores = [0] * num
for _ in range(q):
    prof, qNum, score = [int(x) for x in input().split()]
    qNum -= 1
    if score > maxScores[qNum]:
        final[qNum] = prof
        maxScores[qNum] = score
print(" ".join([str(x) for x in final]))
