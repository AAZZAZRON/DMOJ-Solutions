lines = int(input())
for i in range(lines):
    line = input()
    index = ""
    while line[0].isnumeric():
        index += line[0]
        line = line[1:]
    line = line[1:]
    index = int(index) - 1
    string = line[:index] + line[index + 1:]
    print(i + 1, string)
