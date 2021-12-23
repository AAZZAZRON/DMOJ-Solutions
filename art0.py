import sys
input = lambda: sys.stdin.readline()[:-1]


num = int(input())
for _ in range(num):
    line = input()
    output = ""
    for i in line:
        if i.lower() == "a":
            output += "Hi! "
        elif i.lower() == "e":
            output += "Bye! "
        elif i.lower() == "i":
            output += "How are you? "
        elif i.lower() == "o":
            output += "Follow me! "
        elif i.lower() == "u":
            output += "Help! "
        elif i.isnumeric():
            output += "Yes! "
    print(output)
