numLetters = int(input())
word = input()
count = word.count("C") + word.count("A") + word.count("G") + word.count("U") + word.count("T")
if count != len(word):
    print("neither")
elif "U" in word and "T" in word:
    print("neither")
elif "U" in word:
    print("RNA")
elif "T" in word:
    print("DNA")
elif count == len(word):
    print("both")
else:
    print("neither")
