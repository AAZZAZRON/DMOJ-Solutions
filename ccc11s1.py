numLines = int(input())
s, t = 0, 0
for i in range(numLines):
    x = input().lower()
    s += x.count("s")
    t += x.count("t")
if t > s:
    print("English")
else:
    print("French")
