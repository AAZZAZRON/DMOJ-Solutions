n = int(input())
print(2 * (n // 4) + (1 if n % 4 == 3 else 0))
print("MM__" * (n // 4), end='')
if n % 4 == 1:
    print("_")
elif n % 4 == 2:
    print("__")
elif n % 4 == 3:
    print("M__")