line = input() + "A"
notes = ""
up = 0
v = ""
alpha = "ABCDEFGHIJKLMNOPQRST"
nums = "0123456789"
for i in line:
    if v == "" and i in alpha:
        notes += i
    elif i in "+-":
        up = i == "+"
    elif i in nums:
        v += i
    else:
        print(f"{notes} {'tighten' if up else 'loosen'} {v}")
        notes = i
        v = ""
