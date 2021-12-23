import sys
input = sys.stdin.readline


k, q = [int(x) for x in input().split()]
nums = sorted([int(x) for x in input().split()])
if q == 1 and nums[0] == 0:
    print(-1)
    sys.exit()
if k == 1:
    print(nums[0] if nums[0] != 0 else nums[1])
    sys.exit()
if nums[0] == 0:
    print(str(nums[1]) + "0" * (k - 2) + str(nums[1]))
else:
    print(str(nums[0]) * k)
