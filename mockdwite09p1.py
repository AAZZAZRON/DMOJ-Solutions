from bisect import bisect_left, bisect_right
isSSA = []


def isSuper(n):
    return sum([int(x) for x in str(n)]) % 2 == 0


def isSpecial(n):
    highest = 0
    for i in str(n):
        if int(i) <= highest:
            return False
        highest = int(i)
    return True


def isAwesome(n):
    x = 2
    while x * x <= n:
        if n % (x * x) == 0:
            return False
        x += 1
    return True


for i in range(1, 1000001):
    if isSuper(i) and isSpecial(i) and isAwesome(i):
        isSSA.append(i)

for _ in range(5):
    a, b = [int(x) for x in input().split()]
    start = bisect_left(isSSA, a)
    end = bisect_right(isSSA, b)
    print(end - start)
