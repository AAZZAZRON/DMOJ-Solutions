import sys
input = lambda: sys.stdin.readline()[:-1]
vowels = {"a", "e", "i", "o", "u"}
const = {"k", "r", "m", "n"}
for _ in range(int(input())):
    word = input() + "!"
    l = len(word) - 1
    i = 0
    ans = 1
    while i < l:
        if word[i] in vowels:
            i += 1
        elif word[i] in const and word[i + 1] in vowels:
            i += 2
        elif word[i] == "h" and word[i + 1] in vowels and word[i + 1] != "u":
            i += 2
        elif word[i:i + 2] == "fu":
            i += 2
        else:
            ans = 0
            break
    if ans:
        print("YES")
    else:
        print("NO")