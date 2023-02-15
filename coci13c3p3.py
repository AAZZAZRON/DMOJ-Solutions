nums = []
ones = "one two three four five six seven eight nine ten".split()
elevens = "eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
tens = "twenty thirty forty fifty sixty seventy eighty ninety".split()
nums.extend(ones)
nums.extend(elevens)
for a in tens:
    nums.append(a)
    for b in ones[:-1]:
        nums.append(a + b)
hundred = nums.copy()
for one in ones[:-1]:
    nums.append(f"{one}hundred")
    nums.extend([f"{one}hundred{x}" for x in hundred])


n = int(input())
words = [input() for _ in range(n)]
ind = words.index("$")
l = sum(len(x) for x in words) - 1
for tot in range(1000):
    if l + len(nums[tot]) == tot + 1:
        words[ind] = nums[tot]
        break
print(*words)
