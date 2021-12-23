num = int(input())
cake = [int(x) for x in input().split()]
added = eval("+".join([str(x) for x in cake]))
counter = 0
for x in cake:
    if x != added // num:
        counter += 1
print(counter)
