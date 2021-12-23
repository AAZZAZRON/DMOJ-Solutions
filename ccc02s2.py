num = int(input())
divide = int(input())
whole = num // divide
remainder = num % divide
if remainder == 0:
    print(whole)
else:
    factors1 = [x if divide % x == 0 else 1 for x in range(1, divide + 1)]
    factors2 = [x if remainder % x == 0 else 1 for x in range(1, remainder + 1)]
    one = set(factors1)
    two = set(factors2)
    common = one.difference(one.difference(two))
    add = 1
    if common:
        for x in common:
            add *= x

    if whole == 0:
        print(f"{remainder // add}/{divide // add}")
    else:
        print(f"{whole} {remainder // add}/{divide // add}")
