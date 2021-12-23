import sys
input = sys.stdin.readline


vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
numCases = int(input())
for i in range(numCases):
    one = input().lower()
    one = one.split()[-1]
    for j in range(1, len(one)):
        if one[-j] in vowels:
            one = one[-j:]
            break
    two = input().lower()
    two = two.split()[-1]
    for j in range(1, len(two)):
        if two[-j] in vowels:
            two = two[-j:]
            break
    three = input().lower()
    three = three.split()[-1]
    for j in range(1, len(three)):
        if three[-j] in vowels:
            three = three[-j:]
            break
    four = input().lower()
    four = four.split()[-1]
    for j in range(1, len(four)):
        if four[-j] in vowels:
            four = four[-j:]
            break
    if one == two == three == four:
        print("perfect")
    elif one == two and three == four:
        print("even")
    elif one == three and two == four:
        print("cross")
    elif one == four and two == three:
        print("shell")
    else:
        print("free")
