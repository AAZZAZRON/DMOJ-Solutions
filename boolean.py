list = ["True", "False"]
words = input().split()
if (len(words) - 1) % 2 == 0:
    print(words[-1])
else:
    if words[-1] == list[0]:
        print(list[1])
    else:
        print(list[0])
