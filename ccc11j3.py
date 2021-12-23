def sumac(one, two, len):
    three = one - two
    len += 1
    if three > two:
        print(len)
        return
    else:
        sumac(two, three, len)


first = int(input())
second = int(input())
n = 2
sumac(first, second, n)
