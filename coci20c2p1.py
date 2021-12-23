numChar = int(input())
string = "!" + input()
drawing = [""]
index = 0
for i in range(1, len(string)):
    char = ""
    if string[i] == "+":
        if string[i - 1] == string[i]:
            index -= 1
        char = "/"
    elif string[i] == "-":
        if string[i - 1] == string[i] or string[i - 1] == "=":
            index += 1
        char = "\\"
    elif string[i] == "=":
        if string[i - 1] == "+":
            index -= 1
        char = "_"
    if index == -1:
        drawing.insert(0, "." * len(drawing[0]))
        index = 0
    elif index == len(drawing):
        drawing.append("." * len(drawing[0]))
    for j in range(len(drawing)):
        if j == index:
            drawing[j] += char
        else:
            drawing[j] += "."
for i in drawing:
    print(i)
