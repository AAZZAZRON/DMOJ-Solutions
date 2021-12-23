from math import pi


radius = int(input())
one = pi * radius * radius
one = round(one * 1000000) / 1000000
print(str(one) + "0" * (6 - len(str(one).split(".")[1])))
print(str(2 * radius * radius) + ".000000")

