num, happy = [int(x) for x in input().split()]
answer = [0] * num
complete = False
if num % 2 == 0: # if num is even
    if happy % 2 == 0: # if happy is even
        for i in range(happy, num, 2):
            answer[i] = 1
        complete = True
elif num % 2 == 1: # if num is odd
    if happy % 2 == 1: # if happy is odd
        for i in range(happy + 1, num, 2):
            answer[i] = 1
        complete = True
if complete:
    print(" ".join([str(x) for x in answer]))
else:
    print(-1)
