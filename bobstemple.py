nums = int(input())
numbers = sorted([int(x) for x in input().split()])
up = set()
num = []
for i in numbers:
    if i not in up:
        up.add(i)
    else:
        num.append(i)
print(*up, sep=" ", end="")
num.reverse()
if num:
    print("", end=" ")
print(*num, sep=" ")
