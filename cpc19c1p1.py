n = int(input())
arr = [1]
current = 1
n -= 1
add = True
while n >= 1:
    if add:
        current += n
        add = False
    else:
        current -= n
        add = True
    arr.append(current)
    n -= 1
print(" ".join([str(x) for x in arr]))
