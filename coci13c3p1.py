a = 1
b = 0
for i in range(int(input())):
    x = b
    y = b + a
    a, b = x, y
print(a, b)
