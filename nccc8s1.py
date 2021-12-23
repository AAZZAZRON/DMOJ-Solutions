alphabet = [x for x in input()]
word = input() + "!"
valid = set()
for index in range(0, len(word) - 1):
    valid.add((word[:index] + word[index + 1:])[:-1])
    for letter in alphabet:
        valid.add((word[:index] + letter + word[index + 1:])[:-1])
        valid.add((word[:index] + letter + word[index:])[:-1])
        valid.add((word[:index + 1] + letter + word[index + 1:])[:-1])
valid = list(valid)
valid.sort()
# print(valid)
for i in valid:
    if i != word[:-1] and i != "":
        print(i)
