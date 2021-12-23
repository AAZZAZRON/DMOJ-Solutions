import sys
input = sys.stdin.readline


frequencies = {}
values = {}
numNums = int(input())
for i in range(numNums):
    x = int(input())
    if x in frequencies:
        frequencies[x] += 1
    else:
        frequencies[x] = 1
for i in frequencies.keys():
    if frequencies[i] in values:
        values[frequencies[i]].append(i)
    else:
        values[frequencies[i]] = [i]

keys = sorted(values.keys())
if len(values[keys[-1]]) != 1:
    print(max(values[keys[-1]]) - min(values[keys[-1]]))
else:
    print(max(abs(values[keys[-1]][0] - min(values[keys[-2]])), abs((values[keys[-1]][0] - max(values[keys[-2]])))))
