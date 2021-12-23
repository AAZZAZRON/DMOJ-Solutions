numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
for _ in range(5):
    line = input()
    moves = 0
    maximum = 1
    depth = 1
    sum = 0
    i = 0
    while i < len(line):
        q = line[i]
        if q == "(":
            depth += 1
            maximum = max(maximum, depth)
        elif q == " ":
            pass
        elif q == ")":
            depth -= 1
        else:
            if line[i + 1] in numbers:
                i += 1
                sum += int(q) * 10
            sum += int(line[i])
        moves += 1
        i += 1
    print(moves - maximum, sum)
