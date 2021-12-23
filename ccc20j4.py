'''''''''
def cyclicShift(t, s):
    try:
        t = t.upper()
        s = s.upper()
        s2 = s
        for i in range(1, len(s) + 1):
            first = s[0]
            striping = s.lstrip(first)
            s = striping
            for j in range(1, len(s2) - len(striping) + 1):
                s = s + first
            if s in t:
                print('Yes')
                exit()
            else:
                pass
        print('No')
        exit()
    except ValueError:
        print('You did not type in letters. Please try again.')
        exit()


inputStuff = input('Enter letters: ')
inputWord = input('Enter chosen letters: ')
print(cyclicShift(inputStuff, inputWord))
'''''''''''

T = input()
S = input()

T = T.upper()
S = S.upper()
s2 = S
Y = 'HI'
for i in range(1, len(S) + 1):
    first = S[0]
    striping = S.lstrip(first)
    S = striping
    for j in range(1, len(s2) - len(S)):
        S = first + S
    S = S + first
    if S in T:
        Y = 'yes'
        print('yes')
        break
if Y != 'yes':
    print('no')
