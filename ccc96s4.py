def convertNum(one, two):
    numberOne = 0
    numberTwo = 0
    for j in range(0, len(one) - 1):
        if converter[one[j]] < converter[one[j + 1]]:
            numberOne -= converter[one[j]]
        else:
            numberOne += converter[one[j]]
    numberOne += converter[one[-1]]
    for j in range(0, len(two) - 1):
        if converter[two[j]] < converter[two[j + 1]]:
            numberTwo -= converter[two[j]]
        else:
            numberTwo += converter[two[j]]
    numberTwo += converter[two[-1]]
    finalNum = numberOne + numberTwo
    # print(finalNum)
    return finalNum


def convertBack(final):
    final = [x for x in str(final)]
    tmp = ""
    while final:
        value = int(final.pop(0))
        if value == 9:
            if not final:
                tmp += "IX"
            elif len(final) == 1:
                tmp += "XC"
            else:
                tmp += "CM"
        elif value == 4:
            if not final:
                tmp += "IV"
            elif len(final) == 1:
                tmp += "XL"
            else:
                tmp += "CD"
        else:
            if value < 5:
                if not final:
                    tmp += "I" * value
                elif len(final) == 1:
                    tmp += "X" * value
                else:
                    tmp += "C" * value
            else:
                value -= 5
                if not final:
                    tmp += "V" + "I" * value
                elif len(final) == 1:
                    tmp += "L" + "X" * value
                else:
                    tmp += "D" + "C" * value
    # print(tmp)
    return tmp


converter = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
num = int(input())
for i in range(0, num):
    output = ""
    roman = input()
    output += roman
    roman = roman[:-1]
    romanSplit = roman.split("+")
    numOne = romanSplit[0]
    numTwo = romanSplit[1]
    number = convertNum(numOne, numTwo)
    if number == 1000:
        word = "M"
    elif number > 1000:
        word = "CONCORDIA CUM VERITATE"
    else:
        word = convertBack(number)
    print(f"{roman}={word}")
