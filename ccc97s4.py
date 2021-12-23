for _ in range(int(input())):
    c = 1
    values = {}
    while True:
        line = input().split()
        if not line:
            print("")
            break
        for i in range(len(line)):
            if line[i] in values:
                line[i] = values[line[i]]
            else:
                values[line[i]] = str(c)
                c += 1
        print(" ".join(line))

