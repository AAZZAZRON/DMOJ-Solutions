from sys import stdin
input = stdin.readline


n = int(input())
search = {x for x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"}
for _ in range(n):
    counter = 0
    line = input()[:-1] + "!"
    output = ""
    tmp = ""
    for i in line:
        if i in search:
            tmp += i
            counter += 1
        else:
            if counter == 4:
                output += "****" + i
            else:
                output += tmp + i
            tmp = ""
            counter = 0
    print(output[:-1])
