symbols = "+-*^/%"
equation = input().split()
index = 2
while len(equation) != 1:
    if equation[index] in symbols:
        ind = equation[index]
        if ind == "+":
            equation[index] = str(float(equation[index - 2]) + float(equation[index - 1]))
        elif ind == "-":
            equation[index] = str(float(equation[index - 2]) - float(equation[index - 1]))
        elif ind == "*":
            equation[index] = str(float(equation[index - 2]) * float(equation[index - 1]))
        elif ind == "/":
            equation[index] = str(float(equation[index - 2]) / float(equation[index - 1]))
        elif ind == "^":
            equation[index] = str(float(equation[index - 2]) ** float(equation[index - 1]))
        elif ind == "%":
            equation[index] = str(float(equation[index - 2]) % float(equation[index - 1]))
        equation.pop(index - 2)
        equation.pop(index - 2)
        index = 1
    index += 1
ans = round(float(equation[0]) * 10) / 10
print(ans)
