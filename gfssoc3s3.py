num = int(input())
count = 0
counter = 0
add = 9
if num >= 19:
    num = 18
while num > 0:
    count += add
    counter += 1
    num -= 1
    if counter == 2:
        add *= 10
        counter = 0
print(count % 1000000000)
