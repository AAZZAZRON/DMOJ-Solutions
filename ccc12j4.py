K = int(input())
word = input()
output = ''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while K >= 26:
    K -= 26
while K <= -26:
    K += 26

for i in range(0, len(word)):
    x = word[i]
    formula = 3 * (word.index(x, i) + 1) + K
    y = alphabet.index(x) + 1
    solution = y - formula
    z = solution - 1
    output = output + alphabet[z]
print(output)
