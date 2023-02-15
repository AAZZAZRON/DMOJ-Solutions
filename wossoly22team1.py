import math

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


one, two, three = [[int(x) for x in input().split()] for _ in range(3)]
a, b, c = dist(one, two), dist(one, three), dist(two, three)
s = (a + b + c) / 2
print(math.sqrt(s*(s - a) * (s - b) * (s - c)))
