def convertNum(one):
    numberOne = 0
    oneList = []
    for j in range(0, len(one)):
        oneList.append(converter.get(one[j]))
    for j in range(0, len(oneList)):
        if j < len(oneList) - 1:
            if oneList[j] < oneList[j + 1]:
                numberOne -= oneList[j]
            else:
                numberOne += oneList[j]
        else:
            numberOne += oneList[j]
    print(numberOne)


converter = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
for i in range(5):
    convertNum(input())
