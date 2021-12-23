s = str(int(input()))
t = str(int(input()))
toPrint = "E"
if len(s) > len(t):
    toPrint = "S"
elif len(t) > len(s):
    toPrint = "T"
else:
    for i in range(0, len(s)):
        if int(s[i]) > int(t[i]):
            toPrint = "S"
            break
        if int(s[i]) < int(t[i]):
            toPrint = "T"
            break
print(toPrint)
