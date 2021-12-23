from collections import deque


num = int(input())
remainders = {0: [], 1: [], 2: []}
numbers = [int(x) for x in input().split()]
for i in numbers:
    remainders[i % 3].append(i)
# 0 --> 1, 2
# 1 --> 0, 1
# 2 --> 0, 2
sequence = deque()
zero, one, two = remainders[0], remainders[1], remainders[2]
impossible = False
if not zero and one and two:
    impossible = True
while zero and not impossible:
    sequence.append(zero.pop())
    if one:
        sequence.append(one.pop())
    elif two:
        sequence.append(two.pop())
    elif not zero:
        pass
    else:
        impossible = True
if not impossible:
    if one:
        sequence.extend(one)
    if two:
        sequence.extendleft(two)
if impossible:
    print("impossible")
else:
    print(" ".join([str(x) for x in sequence]))
