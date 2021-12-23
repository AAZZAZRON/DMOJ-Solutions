x = input()
distinct = set()
letterFreq = {x: 0 for x in "abcdefghijklmnopqrstuvwxyz"}
for i in x:
    distinct.add(i)
    letterFreq[i] += 1

counter = 1
for i in distinct:
    counter *= (letterFreq[i] + 1)
print(counter % 1000000007)
