from collections import deque


def reset(one, two, popped):
    while True:
        if len(one) >= 2 and one[0] <= one[1]:
            popped.appendleft(one[0])
            one.popleft()
        else:
            if len(one) < 2:
                popped.appendleft(one[0])
                one.popleft()
            if one:
                popped.appendleft(one[0])
                one.popleft()
            two.extendleft(popped)
            if popped:
                moves.append(len(popped))
            return


n = int(input())
one = deque([int(x) for x in input().split()])
two = deque()
popped = deque()
move = 0
moves = []


while True:
    if not move:
        if len(one) >= 2 and one[0] <= one[1] and two and one[0] <= two[0]:
            popped.appendleft(one[0])
            one.popleft()
        elif not two:
            reset(one, two, popped)
            move = 1
            popped = deque()
        else:
            if (one and one[0] <= two[0]) or (len(one) < 2 and one[0] <= two[0]):
                popped.appendleft(one[0])
                one.popleft()
            two.extendleft(popped)
            if popped:
                moves.append(len(popped))
            popped = deque()
            move = 1
    else:
        if one and two and two[0] <= one[0]:
            popped.appendleft(two[0])
            two.popleft()
        elif not one:
            moves.append(-n)
            break
        else:
            one.extendleft(popped)
            if popped:
                moves.append(-len(popped))
            popped = deque()
            move = 0
    # print(one, two, moves)
assert len(moves) < 7 * n
print(len(moves))
[print(x) for x in moves]
