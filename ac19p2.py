alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
            "t", "u", "v", "w", "x", "y", "z"]
numLetters = int(input())
shift = int(input())
string = []
dictionary = {}
[string.append(x) for x in input()]
for i in alphabet:
    index = alphabet.index(i)
    index += shift
    while index >= 26:
        index -= 26
    dictionary[i] = alphabet[index]
for i in range(numLetters):
    if string[i] in dictionary:
        string[i] = dictionary[string[i]]
string = "".join(string)
print(string)
