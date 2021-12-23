from sys import stdin
input = stdin.readline


num = int(input())
for _ in range(num):
    numbers, final = [int(x) for x in input().split()]
    original = numbers * (numbers + 1) // 2
    find = original - final
    if numbers == 2:
        print(1)
    else:
        if find - 1 <= numbers:
            if find % 2 == 0:
                print(find // 2 - 1)
            else:
                print(find // 2)
        else:
            if find % 2 == 0:
                print(find // 2 - 1 - (find - numbers - 1))
            else:
                print(find // 2 - (find - numbers - 1))
