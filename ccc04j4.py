alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
            "T", "U", "V", "W", "X", "Y", "Z"]

key = []
[key.append(alphabet.index(x)) for x in input()]
string = input()
new = ""
keyCount = 0
for i in string:
    if i in alphabet:
        index = alphabet.index(i) + key[keyCount]
        while index >= 26:
            index -= 26
        new += alphabet[index]
        keyCount += 1
        if keyCount == len(key):
            keyCount = 0
print(new)
