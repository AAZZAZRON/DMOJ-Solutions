start = int(input())
finish = int(input())
count = 0
cannotHave = [2, 3, 4, 5, 7]
for q in range(start, finish):
    q = str(q)
    valid = True
    for i in range(len(q)):
        j = q[i]
        if int(j) in cannotHave:
            valid = False
            break
    if valid:
        reverse = []
        for i in range(len(q)):
            if q[i] == "6":
                reverse.insert(-(i + 1), "9")
            elif q[i] == "9":
                reverse.insert(-(i + 1), "6")
            else:
                reverse.insert(-(i + 1), q[i])
        string = "".join(reverse)
        if string == q:
            count += 1
print(count)
