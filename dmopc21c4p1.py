def getArea(one, two, three):
    return abs(one[0] * (two[1] - three[1]) + two[0] * (three[1] - one[1]) + three[0] * (one[1] - two[1]))


n, q = [int(x) for x in input().split()]
points = [[int(x) for x in input().split()] for _ in range(n)]
for _ in range(q):
    ct = 0
    new = [int(x) for x in input().split()]
    for w in points:
        a = w[:2]
        b = w[2:4]
        c = w[4:]
        if getArea(a, b, c) == getArea(a, b, new) + getArea(a, new, c) + getArea(new, b, c):
            ct += 1
    print(ct)