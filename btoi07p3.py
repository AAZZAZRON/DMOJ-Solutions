from collections import deque


n, m, c = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
maximum = deque()
minimum = deque()
found = 0
for i in range(m):
    v = nums[i]
    while maximum and nums[maximum[-1]] <= v:
        maximum.pop()
    maximum.append(i)

    while minimum and nums[minimum[-1]] >= v:
        minimum.pop()
    minimum.append(i)
if nums[maximum[0]] - nums[minimum[0]] <= c:
    print(1)
    found = 1
for i in range(m, n):
    v = nums[i]
    while maximum and nums[maximum[-1]] <= v:
        maximum.pop()
    maximum.append(i)
    while maximum and maximum[0] <= i - m:
        maximum.popleft()
    while minimum and nums[minimum[-1]] >= v:
        minimum.pop()
    minimum.append(i)
    while minimum and minimum[0] <= i - m:
        minimum.popleft()
    if nums[maximum[0]] - nums[minimum[0]] <= c:
        print(i - m + 2)
        found = 1
if not found:
    print("NONE")

