def alphabet(line, line2, string=""):
    lineCopy = line + ""
    line2Copy = line2 + ""
    possible = []
    if line == "":
        print(string)
        string += "F"
        return string
    for i in letters:
        if letters[i][0] == line[:len(letters[i][0])] and letters[i][1] == line2[:len(letters[i][1])]:
            possible.append(i)
    if not possible:
        return
    for i in possible:
        if "F" not in string:
            line = lineCopy[len(letters[i][0]):]
            line2 = line2Copy[len(letters[i][0]):]
            alphabet(line, line2, string + i)


letters = {"A": ["x.", "xx"], "B": ["xx", "xx"], "C": ["x.x", "xxx"], "D": ["xx", ".x"], "E": ["xxx", ".xx"]}
for i in range(0, 5):
    one = input()
    two = input()
    alphabet(one, two)
