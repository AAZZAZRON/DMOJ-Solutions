'''
Sorting - based on an input, output then from least to greatest
'''

num = int(input())
inputList = []
for i in range(0, num):
    x = int(input())
    inputList.append(x)

inputList.sort()

for i in range(0, len(inputList)):
    print(inputList[i])
