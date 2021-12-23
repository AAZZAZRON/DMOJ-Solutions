for _ in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    solve = 1
    needA = 0
    if c != 0:
        a -= c - 1
        needA = 1
        if a < 0:
            solve = 0
    if solve:
        if needA:
            a -= 1
            if a < 0:
                solve = 0
        else:
            b %= 2
            if b == 1:
                a -= 2
                if a < 0:
                    solve = 0
    if solve:
        if a % 2 == 1:
            solve = 0

    if solve:
        print("YES")
    else:
        print("NO")
