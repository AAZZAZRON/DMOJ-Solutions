numRocks = int(input())
age = [int(x) for x in input().split()]
ages = {}
for i in age:
    if i in ages:
        ages[i] += i
    else:
        ages[i] = i
values = list(ages.values())
max = max(values)
keys = list(ages.keys())
print(keys[values.index(max)])
