from sys import stdin
input = stdin.readline


num = int(input())
words = {x: [] for x in "abcdefghijklmnopqrstuvwxyz'!"}
for _ in range(num):
    word = input()[:-1]
    words[word[0]].append([word, len(word)])
for _ in range(10):
    findWord = input()[:-1] + "!"
    length = len(findWord)
    dp = [999999999] * length
    dp[0] = -1
    for i in range(length):
        if dp[i] != 999999999:
            for word, size in words[findWord[i]]:
                if i + size < length and findWord[i:i + size] == word:
                    dp[i + size] = min(dp[i + size], dp[i] + 1)
    print(dp[-1])
