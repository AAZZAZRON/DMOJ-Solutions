import sys
input = sys.stdin.readline

num = int(input())
cats = 0
dogs = 0
for i in range(0, num):
    x = input()[:-1]
    if x == "cats":
        cats += 1
    elif x == "dogs":
        dogs += 1
if cats > dogs:
    print("cats")
elif dogs > cats:
    print("dogs")
else:
    print("equal")
