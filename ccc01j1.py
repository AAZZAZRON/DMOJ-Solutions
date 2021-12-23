x = int(input())
star = "*"
picture = []
numStars = 1
middle = False
while True:
    line = " " * 2 * x
    if not middle:
        line = line[numStars + numStars:]
        line = "*" * numStars + line + "*" * numStars
        picture.append(line)
        numStars += 2
        if numStars == x:
            middle = True
    else:
        line = "*" * x * 2
        picture.append(line)
        break
for i in picture:
    print(i)
del picture[-1]
for i in range(1, len(picture) + 1):
    print(picture[-i])
