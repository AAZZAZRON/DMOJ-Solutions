x = int(input())
scores = [float(x) for x in input().split()]
scores.sort()
frequency = {}
before = -1
count = 0
mean = 0
for i in scores:
    mean += i
    if i == before:
        count += 1
    else:
        if count not in frequency:
            frequency[count] = []
        frequency[count].append(before)
        before = i
        count = 1
if count not in frequency:
    frequency[count] = []
frequency[count].append(before)
mean /= x
print(round(mean * 10) // 10)
if x % 2 == 0:
    median = (scores[x // 2 - 1] + scores[x // 2]) / 2
else:
    median = scores[x // 2]
print(round(median * 10) // 10)
# print(frequency)
numbers = frequency[max(frequency.keys())]
print(" ".join(str(round(x * 10) // 10) for x in numbers))
