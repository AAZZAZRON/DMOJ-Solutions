before = "T"
count = 0
for i in range(7):
    x = input()
    if before == "J" and x == "T":
        count += 1
    before = x
if before == "J":
    count += 1
print(count)