rotaters = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
word = input()
for i in range(0, len(word)):
    if word[i] in rotaters:
        pass
    else:
        print('NO')
        break
    if i == len(word) - 1:
        print('YES')
