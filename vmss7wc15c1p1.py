x = input().split("-")
one = eval("+".join([y for y in x[0]]))
two = eval("+".join([y for y in x[1]]))
three = eval("+".join([y for y in x[2]]))
if one == two == three:
    print("Goony!")
else:
    print("Pick up the phone!")
