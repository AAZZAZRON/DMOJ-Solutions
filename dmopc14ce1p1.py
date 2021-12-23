verb = input()
noun = input()
if noun[-1] == 's':
    x = "les"
elif noun[-1] == "e":
    x = "la"
else:
    x = "le"
print(f"{verb}-tu {x} {noun} ?")
