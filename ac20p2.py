from sys import stdin
input = stdin.readline


number, moves = [int(x) for x in input().split()]
weights = {}
theWeight = [int(x) for x in input().split()]
for i in theWeight:
    if i not in weights:
        weights[i] = 1
    else:
        weights[i] += 1
for i in range(moves):
    move, num = [int(x) for x in input().split()]
    if move == 1:
        if num not in weights:
            continue
        if num % 2 == 1:
            if num // 2 not in weights:
                weights[num // 2] = weights[num]
            else:
                weights[num // 2] += weights[num]
            if num // 2 + 1 not in weights:
                weights[num // 2 + 1] = weights[num]
            else:
                weights[num // 2 + 1] += weights[num]
        else:
            if num // 2 not in weights:
                weights[num // 2] = weights[num] * 2
            else:
                weights[num // 2] += weights[num] * 2
        weights[num] = 0
    else:
        if num in weights:
            print(weights[num])
        else:
            print(0)
