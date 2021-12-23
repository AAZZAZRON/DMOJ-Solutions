l, h, w = [int(x) for x in input().split()]
d = int(input()) / 2
PI = 3.14159
print(l * h * w - PI * d * d * h)
