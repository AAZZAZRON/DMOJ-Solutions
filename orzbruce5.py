from sys import stdin
input = stdin.readline


num, queries, length = [int(x) for x in input().split()]
dp_dictionary = {}

for q in range(num):
    word = input()[:-1]
    dp = [[False] * length for _ in range(length)]
    for i in range(length - 1, -1, -1):
        letter = word[i]
        for j in range(i, length):
            if i == j:
                dp[i][j] = True
            elif letter == word[j]:
                if dp[i + 1][j - 1] or abs(j - i) == 1:
                    dp[i][j] = True
    dp_dictionary[q] = dp


right = [True] * num
queries = {tuple(int(x) - 1 for x in input().split()) for _ in range(queries)}
for start, end in queries:
    for i in range(num):
        right[i] = right[i] and dp_dictionary[i][start][end]
counter = 0
for i in right:
    if i:
        counter += 1
print(counter)
