a, b = [int(x) for x in input().split()]
c, d = [int(x) for x in input().split()]
if a == c:
    print("y-axis")
elif b == d:
    print("x-axis")
else:
    print("neither")