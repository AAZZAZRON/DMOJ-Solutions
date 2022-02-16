import sys
input = sys.stdin.readline


n = int(input())
nums = [0] * n
arr = [0] * n
for i in range(n - 1):
    print("?", i + 1, i + 2)
    sys.stdout.flush()
    arr[i] = int(input())

for q in range(-1, n):
    if arr[q] <= n and arr[q + 1] <= n:
        used = {0, 1}
        ind = q
        done = 1
        nums[ind + 1] = 1
        for i in range(ind + 1, n - 1):
            nums[i + 1] = arr[i] // nums[i]
            if nums[i + 1] > n or nums[i + 1] in used:
                done = 0
                break
            used.add(nums[i + 1])
        if done:
            for i in range(ind, -1, -1):
                nums[i] = arr[i] // nums[i + 1]
                if nums[i] > n or nums[i] in used:
                    done = 0
                    break
                used.add(nums[i])
        if done:
            break
print("!", *nums)