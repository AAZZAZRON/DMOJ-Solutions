from sys import stdin
input = stdin.readline


def update(array, index, val, maximum):
    while index <= maximum:
        array[index] += val
        index += index & (-index)


def getSum(array, index):
    total = 0
    while index > 0:
        total += array[index]
        index -= index & (-index)
    return total


size, m = [int(x) for x in input().split()]
sumBIT = [0] * (size + 1)
freqBIT = [0] * 1000001
nums = [0] + [int(x) for x in input().split()]
for i in range(1, size + 1):
    update(sumBIT, i, nums[i], size)
    update(freqBIT, nums[i], 1, 1000000)
print(sumBIT)
for i in range(m):
    query, *stuff = input().split()
    if query == "C":
        ind, changeTo = [int(x) for x in stuff]
        update(sumBIT, ind, changeTo - nums[ind], size)
        update(freqBIT, nums[ind], -1, 1000000)
        update(freqBIT, changeTo, 1, 1000000)
        nums[ind] = changeTo
    elif query == "S":
        l, r = [int(x) for x in stuff]
        print(getSum(sumBIT, r) - getSum(sumBIT, l - 1))
    else:
        print(getSum(freqBIT, int(stuff[0])))
