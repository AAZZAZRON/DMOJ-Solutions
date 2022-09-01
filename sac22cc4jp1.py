w = input()
ct = 0
for i in "aeiouy":
    ct += w.count(i)
print("good" if ct >= 2 else "bad")