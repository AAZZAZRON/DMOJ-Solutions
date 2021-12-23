words = []
lines = input()
before = ""
current = ""
for i in lines:
    if i == "A":
        val = "V"
    else:
        val = "C"
    if val == before:
        words.append(current)
        current = i
    else:
        current += i
    before = val
words.append(current)
print(" ".join(words))
