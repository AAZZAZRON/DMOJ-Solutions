import sys
input = lambda: sys.stdin.readline()[:-1]


def traverse(word, memo=None):
    if memo is None:
        memo = {}
    if word in memo:
        return memo[word]
    elif word == "":
        return 1
    counter = 0
    wordL = len(word)
    for check, length in search:
        if length <= wordL and word[:length] == check:
            counter += traverse(word[length:], memo)
    memo[word] = counter
    return counter


search = [["ook", 3], ["ookook", 6], ["oog", 3], ["ooga", 4], ["ug", 2],
          ["mook", 4], ["mookmook", 8], ["oogam", 5],
          ["oogum", 5], ["ugug", 4]]
for _ in range(10):
    line = input()
    print(traverse(line))

