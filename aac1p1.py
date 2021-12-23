l, r = [float(x) for x in input().split()]
square = l * l
circle = 3.14 * r * r
if square > circle:
    print("SQUARE")
else:
    print("CIRCLE")
