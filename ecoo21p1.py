from sys import exit
start = int(input())
interval = int(input())
message = int(input())
for i in range(3):
    start += interval
    if start >= message:
        print(start)
        exit()
print("Who knows...")
