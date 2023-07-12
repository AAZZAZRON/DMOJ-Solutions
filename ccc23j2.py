m = {"P": 1500, "M": 6000, "S": 15500, "C": 40000, "T": 75000, "H": 125000}
ct = sum(m[input()[0]] for _ in range(int(input())))
print(ct)