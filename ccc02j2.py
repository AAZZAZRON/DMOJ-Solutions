import sys
input = sys.stdin.readline


vowel = ["a", "e", "i", "o", "u", "y"]
while True:
    word = input()[:-1]
    if word == "quit!":
        break
    if len(word) > 4:
        if word[-2:] == "or" and word[-3] not in vowel:
            print(word[:-1] + "ur")
        else:
            print(word)
    else:
        print(word)
