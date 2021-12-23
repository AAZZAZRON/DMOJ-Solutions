N = int(input())

for i in range(0, N):
    x = 0
    message = input()
    dup = message
    real = message
    len_real = len(real)
    first_character = message[0]
    message = message.lstrip(first_character)
    message = message + '|'
    length = int(len_real) - int(len(message) - 1)
    for j in range(0, length):
        message = message + first_character
    x = x + length
    word = str(length) + ' ' + first_character
    z = 1
    while x < int(len_real):
        z += 1
        dup = message
        first_character = message[0]
        message = message.lstrip(first_character)
        message = message + '|'
        length = int(len_real) - int(len(message) - z)
        for j in range(0, length):
            message = message + first_character
        x = x + length
        if first_character == '|':
            pass
        else:
            word = word + ' ' + str(length) + ' ' + first_character
    print(word)
