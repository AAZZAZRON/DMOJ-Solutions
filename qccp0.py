import sys
input = sys.stdin.readline


for _ in range(int(input())):
    tmp = float(input())
    if tmp < 34:
        print("Too cold, please try again.")
    elif 34 <= tmp <= 35.5:
        print("Take a hot bath.")
    elif 35.5 < tmp <= 38:
        print("Rest if feeling unwell.")
    elif 38 < tmp <= 39:
        print("Take some medicine.")
    elif 39 < tmp <= 41:
        print("Take a cold bath and some medicine.")
    elif 41 < tmp <= 46.1:
        print("Go to the hospital.")
    elif 46.1 < tmp <= 50:
        print("Congrats, you have a new world record!")
    else:
        print("Too hot, please try again.")