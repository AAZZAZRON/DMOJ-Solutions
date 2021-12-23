import sys
input = sys.stdin.readline


def isMonkey(word):
    done = False
    if word == "":
        pass
    elif word[0] == "A":
        if word == "A":
            done = True
        elif word[1] == "N":
            done = isMonkey(word[2:])
    elif word[0] == "B":
        if word == "BS" or word == "B":
            pass
        else:
            word += "!"
            ind = 0
            while word[ind:].count("S") != 0 and not done:
                index = word[ind:].index("S")
                ind += index + 1
                done = isMonkey(word[1:ind - 1])
                if done and word[ind:] != "!":
                    done = isMonkey("A" + word[ind:-1])
    return done


while True:
    string = input()[:-1]
    if string == "X":
        break
    if isMonkey(string):
        print("YES")
    else:
        print("NO")
