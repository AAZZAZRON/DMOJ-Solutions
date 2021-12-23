letters = "".join(input().split())
word = "".join(input().split())
letters = [x for x in letters]
word = [x for x in word]
letters.sort()
word.sort()
if letters == word:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
