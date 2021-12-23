books = [x for x in input()]
numL, numM, numS = 0, 0, 0
for i in books:
    if i == "L":
        numL += 1
    elif i == "M":
        numM += 1
    else:
        numS += 1
sInL, mInL, sInM, lInM, mInS, lInS = 0, 0, 0, 0, 0, 0
for i in range(0, len(books)):
    val = books[i]
    if i < numL:
        if val == "M":
            mInL += 1
        elif val == "S":
            sInL += 1
    elif i < numL + numM:
        if val == "S":
            sInM += 1
        elif val == "L":
            lInM += 1
    else:
        if val == "M":
            mInS += 1
        elif val == "L":
            lInS += 1
counter = 0
counter += min(sInL, lInS)
counter += min(mInS, sInM)
counter += min(mInL, lInM)
numbers = [sInL, lInS, mInS, sInM, mInL, lInM]
numbers[0] -= lInS
numbers[1] -= sInL
numbers[2] -= sInM
numbers[3] -= mInS
numbers[4] -= lInM
numbers[5] -= mInL
counter += (eval("+".join([str(x) for x in numbers if x >= 0]))) * 2/3
print(int(counter))
