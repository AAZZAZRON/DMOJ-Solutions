from sys import stdin
input = stdin.readline


cases = int(input())
for _ in range(cases):
    nD, num = [int(x) for x in input().split()]
    numbers = [0] * num
    lists = []
    for x in range(nD):
        doors = [int(x) for x in input().split()]
        for i in range(num):
            if x != 0:
                lists[i].append(doors[i])
            else:
                lists.append([doors[i]])
    for doors in lists:
        minimum = min(numbers)
        index = numbers.index(minimum)
        numbers.pop(index)
        second = min(numbers)
        for i in range(nD):
            if i != index:
                doors[i] += minimum
            else:
                doors[i] += second
        numbers = doors
        # print(numbers)
    print(min(numbers))
