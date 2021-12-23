from sys import stdin
input = stdin.readline


days = [[] for _ in range(100001)]
people = int(input())
places = [0] + [int(x) for x in input().split()]
queries = []
q = int(input())
counter = 0
for _ in range(q):
    command, x, y = input().split()
    x = int(x)
    y = int(y)
    if command == "C":
        queries.append((x, y))
    else:
        days[y].append((x, counter))
        counter += 1
answers = [0] * counter
num = 0
for find, i in days[num]:
    answers[i] = places[find]
for x, y in queries:
    num += 1
    places[x] = y
    for find, i in days[num]:
        answers[i] = places[find]
[print(x) for x in answers]
