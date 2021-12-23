import sys
input = sys.stdin.readline


people, rounds = [int(x) for x in input().split()]
scores = {}
worst = {}
for i in range(1, people + 1):
    scores[i] = 0
    worst[i] = 1
for i in range(rounds):
    numbers = [int(x) for x in input().split()]
    for j in range(1, people + 1):
        scores[j] += numbers[j - 1]
    now = list(scores.values())
    sort = now.copy()
    sort.sort()
    sort.reverse()
    for ind in range(len(now)):
        num = now[ind]
        index = sort.index(num) + 1
        if worst[ind + 1] < index:
            worst[ind + 1] = index
    # print(scores, worst)

keys = list(scores.keys())
values = list(scores.values())
now = values.copy()
now.sort()
while now[-1] in values:
    print(f"Yodeller {keys[values.index(now[-1])]} is the TopYodeller: score {scores[keys[values.index(now[-1])]]}, worst rank {worst[keys[values.index(now[-1])]]}")
    values[values.index(now[-1])] = -1
