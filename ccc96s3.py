def permute(number):
    done = False
    numOnes = 0
    print(number)
    oneNum = numOne
    for k in range(1, numOne + 1):
        if number[-k] == "1":
            if k == numOne:
                done = True
                break
        else:
            break
    if done:
        return done
    else:
        leave = False
        k = -1
        reset = ""
        while k < len(number) - 1:
            k += 1
            if number[k] == "1":
                numOnes += 1
            if numOnes == oneNum and len(number) - 1 - numOne + oneNum != k:
                number = number[:k] + "0" + number[k + 1:]
                number = number[:k + 1] + "1" + number[k + 2:]
                while oneNum < numOne:
                    reset = reset + "1"
                    oneNum += 1
                if reset != "":
                    number = number[:k + 2] + reset
                for m in range(len(number), length):
                    number = number + "0"
                leave = True
                numOnes += 1
            elif numOnes == oneNum:
                oneNum -= 1
                numOnes = -1
                k = -1
                numOnes += 1
            if leave:
                break
        return permute(number)


num = int(input())
for i in range(0, num):
    x = input()
    xSplit = x.split()
    finalStr = ""
    length = int(xSplit[0])
    numOne = int(xSplit[1])
    for j in range(0, numOne):
        finalStr = finalStr + "1"
    for j in range(0, length - numOne):
        finalStr = finalStr + "0"
    print("The bit patterns are")
    if numOne == 0 or length - numOne == 0:
        print(finalStr)
    else:
        permute(finalStr)
