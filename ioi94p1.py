import sys
input = sys.stdin.readline


def findMax(on, goTo, memo=None):
    if memo is None:
        memo = {}
    if on == 1:
        return triangle[on][0]
    keep = []
    for x in goTo:
        num = triangle[on][x]
        if (on, x) not in memo:
            if x == 0:
                memo[(on, x)] = findMax(on - 1, [x], memo)
            elif x == on - 1:
                memo[(on, x)] = findMax(on - 1, [x - 1], memo)
            else:
                memo[(on, x)] = findMax(on - 1, [x - 1, x], memo)
        num += memo[(on, x)]
        keep.append(num)
    return max(keep)


layers = int(input())
triangle = {}
for i in range(1, layers + 1):
    triangle[i] = [int(x) for x in input().split()]
print(findMax(layers, [x for x in range(0, layers)]))
