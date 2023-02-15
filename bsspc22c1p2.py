for _ in range(int(input())):
    a, b = input().split()
    if len(a) == 1:
        a = "0" + a
    if len(b) == 1:
        b = "0" + b
    x, y = 0, 0
    if a[-1] == "7" and a[-2] != "1":
        x = 1
    elif a[-2:] == "11":
        x = 2
    if b[-1] == "7" and b[-2] != "1":
        y = 1
    elif b[-2:] == "11":
        y = 2
    x, y = min(x, y), max(x, y)
    print("YES" if x == 1 and y == 2 else "NO")
