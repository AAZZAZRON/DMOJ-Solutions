import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    if a == 1:
        print("bad")
    elif b == 1:
        if a >= 7:
            print("good")
        else:
            print("bad")
    else:
        print("good" if (a >= 4 or b >= 4) else "bad")
