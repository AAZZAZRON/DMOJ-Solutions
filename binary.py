for _ in range(int(input())):
    n = int(input())
    b = bin(n).split("b")[1]
    if (len(b) % 4) == 0:
        t = 0
    else:
        t = 4 - (len(b) % 4)
    b = "0" * t + b
    for i in range(0, len(b), 4):
        print(b[i:i + 4], end="")
        if i + 4 < len(b):
            print(" ", end="")
        else:
            print()
