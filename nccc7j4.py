word = input()
letters = {}
for i in word:
    if i in letters:
        letters[i] += 1
    else:
        letters[i] = 1
word = input()
for i in word:
    if i in letters:
        if letters[i] != 0:
            letters[i] -= 1
print(eval("+".join(str(x) for x in list(letters.values()))))
