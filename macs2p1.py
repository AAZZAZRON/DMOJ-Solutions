dir = ['N', 'E', 'S', 'W']
s = input()
ct = 0
ct -= int(input())
ct += int(input())
print(dir[(dir.index(s) + ct) % 4])