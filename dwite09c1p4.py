for i in range(5):
    word = input()
    for j in word:
        if word.count(j) == 1:
            print(j)
            break
