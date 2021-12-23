code = input().split()
n = int(input())
word = ""
for i in [int(x) for x in input().split()]:
    word += code[i]
print(word)