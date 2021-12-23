time = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3, 'g': 1, 'h': 2, 'i': 3, 'j': 1, 'k': 2, 'l': 3, 'm': 1, 'n': 2,
        'o': 3, 'p': 1, 'q': 2, 'r': 3, 's': 4, 't': 1, 'u': 2, 'v': 3, 'w': 1, 'x': 2, 'y': 3, 'z': 4}
same = {'a': ["a", "b", "c"], 'b': ["a", "b", "c"], 'c': ["a", "b", "c"], 'd': ["d", "e", "f"], 'e': ["d", "e", "f"],
        'f': ["d", "e", "f"], 'g': ["g", "h", "i"], 'h': ["g", "h", "i"], 'i': ["g", "h", "i"], 'j': ["j", "k", "l"],
        'k': ["j", "k", "l"], 'l': ["j", "k", "l"], 'm': ["m", "n", "o"], 'n': ["m", "n", "o"], 'o': ["m", "n", "o"],
        'p': ["p", "q", "r", "s"], 'q': ["p", "q", "r", "s"], 'r': ["p", "q", "r", "s"], 's': ["p", "q", "r", "s"],
        't': ["t", "u", "v"], 'u': ["t", "u", "v"], 'v': ["t", "u", "v"], 'w': ["w", "x", "y", "z"],
        'x': ["w", "x", "y", "z"], 'y': ["w", "x", "y", "z"], 'z': ["w", "x", "y", "z"]}
while True:
    x = input()
    if x == "halt":
        break
    count = 0
    before = []
    for i in x:
        if i in before:
            count += 2
        count += time[i]
        before = same[i]
    print(count)
