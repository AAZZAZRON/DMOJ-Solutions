import sys


val = int(input())
numbers = [x for x in range(1, val + 1)]
cannotBe = {x: set() for x in range(1, val + 1)}
while True:
    print(" ".join([str(x) for x in numbers]))
    sys.stdout.flush()
    val = int(input())
    if val == 0 or val == -1:
        break
    cannotBe[val].add(numbers[val - 1])
    for q in range(len(numbers)):
        i = numbers[q]
        if i != numbers[val - 1] and i not in cannotBe[val]:
            numbers[q] = numbers[val - 1]
            numbers[val - 1] = i
            break
