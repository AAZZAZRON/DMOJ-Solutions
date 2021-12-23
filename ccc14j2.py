num = int(input())
votes = input()
list = []
for i in range(0, num):
    list.append(votes[i])
x = list.count('A')
y = list.count('B')

if x > y:
    print('A')
elif x < y:
    print('B')
else:
    print('Tie')
