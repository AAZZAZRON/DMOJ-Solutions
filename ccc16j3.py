word = "!" + input() + "@"
longest = 0
for i in range(1, len(word) - 1):
    length = 1
    while True: # check odd letter palindromes
        if word[i + length] == word[i - length]:
            if 2 * length + 1 > longest:
                longest = 2 * length + 1
            length += 1
        else:
            break
    length = 1
    while True: # check even letter palindromes
        if word[i - length + 1] == word[i + length]:
            if 2 * length > longest:
                longest = 2 * length
            length += 1
        else:
            break
print(longest)
