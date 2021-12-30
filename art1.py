def mountain(size):
    r = [""] * size
    dist = size - 1
    for i in range(1, size + 1):
        r[i - 1] = " " * dist + "^ " * i + " " * dist
        dist -= 1
    return r


n = int(input())
vals = [int(x) for x in input().split()]
maximum = max(vals)
build = [""] * maximum

for i in vals:
    m = mountain(i)
    wait = maximum - i
    for j in range(maximum):
        if j < wait:
            build[j] += " " * (2 * i)
        else:
            build[j] += m[j - maximum + i]
[print(x) for x in build]
