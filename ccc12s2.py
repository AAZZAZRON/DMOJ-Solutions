string = input()
converter = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
letters = ["I", "V", "X", "L", "C", "D", "M"]
value = 0
for i in range(0, len(string), 2):
    num = int(string[i])
    val = string[i + 1]
    if i + 2 != len(string):
        if letters.index(val) < letters.index(string[i + 3]):
            value -= num * converter[val]
        else:
            value += num * converter[val]
    else:
        value += num * converter[val]
print(value)
