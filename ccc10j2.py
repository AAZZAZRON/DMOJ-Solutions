a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
s = int(input())
aTotal = 0
bTotal = 0
aTally = 0
bTally = 0

while aTally < s:
    aTotal = aTotal + a1 - a2
    aTally = aTally + a1 + a2

while bTally < s:
    bTotal = bTotal + b1 - b2
    bTally = bTally + b1 + b2


if aTally == s:
    pass
elif aTally != s:
    x = aTally - s
    if x >= a2:
        aTotal = aTotal + a2 - x + a2
    else:
        aTotal += x

if bTally == s:
    pass
elif bTally != s:
    x = bTally - s
    if x >= b2:
        bTotal = bTotal + b2 - x + b2
    else:
        bTotal += x

if aTotal > bTotal:
    print('Nikky')
elif bTotal > aTotal:
    print('Byron')
else:
    print('Tied')
