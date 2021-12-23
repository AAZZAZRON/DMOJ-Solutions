import sys
input = sys.stdin.readline


messages = int(input())
for i in range(messages):
    count = 0
    message = input().split("<3")
    count += len(message)
    print(("<3 " * count)[:-1])
