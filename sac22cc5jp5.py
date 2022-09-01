import sys
input = lambda: sys.stdin.readline()[:-1]


n = int(input())
words = []
for _ in range(n):
    word = input()
    ct = 0
    for i in range(len(word) - 1):
        ct += (word[i] == word[i + 1])
    words.append([word, ct])

# let dp[i] be the max substring # ending up until i
maxLetters = [-1] * 26
dp = [0] * (n + 1)
for i in range(1, n + 1):
    word, ct = words[i - 1]
    dp[i] = dp[i - 1] + ct  # assume not the same character
    if maxLetters[ord(word[0]) - ord('a')] != -1:  # find same character
        dp[i] = max(dp[i], maxLetters[ord(word[0]) - ord('a')] + ct + 1)
    maxLetters[ord(word[-1]) - ord('a')] = max(maxLetters[ord(word[-1]) - ord('a')], dp[i])
print(dp[-1])
#print(dp)
# print(maxLetters)