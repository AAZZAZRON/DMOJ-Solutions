def rotate(one, two, x1, y1, x2, y2):
    mX = (x2 - x1) / 2 + x1
    mY = (y2 - y1) / 2 + y1
    one -= mX
    two -= mY
    x = -two + mX
    y = one + mY
    return [int(x), int(y)]


n, k, q = [int(x) for x in input().split()]
queries = [[int(x) for x in input().split()] for _ in range(k)]
for _ in range(q):
    coord = [int(x) for x in input().split()]
    search = coord.copy()
    for a, b, c, d in queries[::-1]:
        if a <= search[0] <= c and b <= search[1] <= d:
            search = rotate(search[0], search[1], a, b, c, d)
    print((search[0] - 1) * n + search[1])
