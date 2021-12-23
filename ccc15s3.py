from sys import stdin
input = stdin.readline
num = int(input())
used = [0] * (num + 1)
val = int(input())
done = False
counter = 0
while not done and counter < val:
    dock = int(input())
    while dock > 0 and used[dock] > 0:
        tmp = used[dock]
        used[dock] += 1
        dock -= tmp
    if dock <= 0:
        done = True
        break
    used[dock] = 1
    counter += 1
print(counter)
