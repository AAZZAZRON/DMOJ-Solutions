n = int(input())
nums = [int(x) for x in input().split()]
print(" ".join([str(x) for x in nums]))

for i in range(n):
    for j in range(n - 1):
        if nums[j] > nums[j + 1]:
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp
            print(" ".join([str(x) for x in nums]))
