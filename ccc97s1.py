from sys import stdin
input = stdin.readline


cases = int(input())
for i in range(cases):
    one = int(input())
    two = int(input())
    three = int(input())
    word1 = [input()[:-1] for j in range(one)]
    word2 = [input()[:-1] for k in range(two)]
    word3 = [input()[:-1] for l in range(three)]
    for x in word1:
        for y in word2:
            for z in word3:
                print(f"{x} {y} {z}.")
