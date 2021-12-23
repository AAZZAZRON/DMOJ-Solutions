length = int(input())

for i in range(0, length):
    message = input()
    message_split = message.split()
    for j in range(0, int(message_split[0]) - 1):
        print(message_split[1], end='')
    print(message_split[1])
