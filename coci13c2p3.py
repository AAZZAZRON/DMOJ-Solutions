blinks = int(input())
word = input()
length = len(word)
original = word
perms = [word]
for _ in range(length):
    new = ""
    for i in range(length // 2):
        new += word[i]
        new += word[-(i + 1)]
    if length % 2 == 1:
        new += word[length // 2]
    word = new
    if word == original:
        break
    perms.append(word)
blinks %= len(perms)
print(perms[-blinks])
