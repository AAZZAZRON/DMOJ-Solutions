simple = input()
encrypt = input()
decoder = {}
for i in range(len(encrypt)):
    letter = encrypt[i]
    if letter not in decoder:
        decoder[letter] = simple[i]
# print(decoder)
phrase = input()
word = ""
for i in phrase:
    if i not in decoder:
        word += "."
    else:
        word += decoder[i]
print(word)
