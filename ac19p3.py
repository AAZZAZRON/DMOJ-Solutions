equation = input()
equation = "".join(equation.split("+"))
equation = "".join(equation.split(")"))
equation = "".join(equation.split("("))
print(sum([int(x) for x in equation.split()]))
