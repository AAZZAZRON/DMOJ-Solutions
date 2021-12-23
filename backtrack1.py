def palindrome(num):
    if memo[num]:
        return memo[num]
    count = 1
    final = num
    while 2 <= num:
        num -= 2
        count += palindrome(num)
    memo[final] = count
    return count


memo = [0] * 64
n = int(input())
print(palindrome(n))
