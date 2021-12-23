from sys import stdin
input = stdin.readline


def encode(phrase):
    sentence = ""
    phrase = phrase.split()
    index = 0
    lengths = [len(x) for x in phrase]
    done = False
    while not done:
        done = True
        for x in range(len(phrase)):
            if index < lengths[x]:
                sentence += phrase[x][index]
                done = False
        index += 1
    words = []
    index = 0
    for length in lengths:
        words.append(sentence[index:index + length])
        index += length
    print(" ".join(words))
    return


def decode(phrase):
    phrase = phrase.split()
    sentence = ["" for _ in range(len(phrase))]
    index = 0
    lengths = [len(x) for x in phrase]
    for word in phrase:
        for letter in word:
            while True:
                if len(sentence[index]) < lengths[index]:
                    sentence[index] += letter
                    index += 1
                    if index == len(phrase):
                        index = 0
                    break
                index += 1
                if index == len(phrase):
                    index = 0
    print(" ".join(sentence))
    return


for _ in range(10):
    command = input()[:-1]
    phrase = input()[:-1]
    if command == "encode":
        encode(phrase)
    else:
        decode(phrase)
