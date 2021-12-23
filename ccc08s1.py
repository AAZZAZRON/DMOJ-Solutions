city = ""
cold = 300
while True:
    try:
        x = input()
        if x == "":
            break
        x = x.split()
    except EOFError:
        break
    if int(x[1]) < cold:
        cold = int(x[1])
        city = x[0]
print(city)
