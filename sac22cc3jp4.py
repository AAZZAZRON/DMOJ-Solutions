def toTen(base, num):
    return int(str(num), base)


def fromTen(base, num):
    r = ""
    while num != 0:
        r += str(num % base)
        num //= base
    return int(r[::-1])


for _ in range(int(input())):
    b1, n, b2 = [int(x) for x in input().split()]
    print(fromTen(b2, toTen(b1, n)))
