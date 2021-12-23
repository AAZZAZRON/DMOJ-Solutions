import sys
input = sys.stdin.readline


numQ = int(input())
student = []
right = 0
for i in range(numQ):
    answer = input()
    student.append(answer)
for i in range(numQ):
    rightAns = input()
    if student[i] == rightAns:
        right += 1
print(right)
