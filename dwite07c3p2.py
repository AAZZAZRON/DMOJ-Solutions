for _ in range(5):
    line = input()
    ans = ""
    i = 0
    while i < len(line) - 1:
        if line[i] == "\'":
            ind = line[i + 1:].index("\'") + i + 1
            ans += " " + line[i + 1:ind]
            i = ind
        elif line[i] == "\"":
            ind = line[i + 1:].index("\"") + i + 1
            ans += " " + line[i + 1:ind]
            i = ind
        elif line[i] == "/" and line[i + 1] == "/":
            ans += " " + line[i + 2:]
            i = len(line) + 1
        elif line[i] == "/" and line[i + 1] == "*":
            ind = line[i + 2:].index("*/") + i + 2
            ans += " " + line[i + 2:ind]
            i = ind
        i += 1
    print(ans[1:])