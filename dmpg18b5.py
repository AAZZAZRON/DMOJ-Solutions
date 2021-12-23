string = input()
length = int(input())
counter = 0
total = 0
before = ""
for i in string:
    if i != before:
        if counter >= length:
            total += (counter - length) + 1
        counter = 1
    else:
        counter += 1
    before = i
if counter >= length:
    total += (counter - length) + 1
print(total)
