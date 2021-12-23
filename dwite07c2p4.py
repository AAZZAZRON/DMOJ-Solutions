for i in range(5):
    x = input()
    needed = ["!"]
    balanced = True
    for j in x:
        if j == "(":
            needed.append(")")
        elif j == "[":
            needed.append("]")
        elif j == "{":
            needed.append("}")
        elif j == ")":
            if needed[-1] == ")":
                needed.pop()
            else:
                balanced = False
                break
        elif j == "]":
            if needed[-1] == "]":
                needed.pop()
            else:
                balanced = False
                break
        elif j == "}":
            if needed[-1] == "}":
                needed.pop()
            else:
                balanced = False
                break
    if balanced:
        print("balanced")
    else:
        print("not balanced")
