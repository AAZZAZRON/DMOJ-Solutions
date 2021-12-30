x, y = [int(x) for x in input().split()]
print(str(x * y // 2) + (".0" if (x * y) % 2 == 0 else ".5"))