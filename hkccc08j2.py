for _ in range(int(input())):
    n = input()
    while len(n) > 1:
        n = str(sum([int(x) for x in n]))
    print(n)