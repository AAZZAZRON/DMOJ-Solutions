from collections import deque


start = int(input())
end = int(input())
counter = 0
beenTo = deque()
beenTo.append(0)

while True:
    num = beenTo.popleft()
    if start <= num * 16 + 10 <= end:
        counter += 1
    if start <= num * 16 + 12 <= end:
        counter += 1
    if start <= num * 16 + 14 <= end:
        counter += 1
    beenTo.append(num * 16 + 10)
    beenTo.append(num * 16 + 12)
    beenTo.append(num * 16 + 14)
    if num * 16 + 14 > end:
        break
print(counter)
