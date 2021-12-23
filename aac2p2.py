from sys import stdin, exit
input = stdin.readline


num = int(input())
numbers = sorted(int(x) for x in input().split())
freq = {}
if num == 2 and numbers[0] != numbers[1]:
    if ((numbers[0] + numbers[1]) / 2) % 1 == 0:
        print(2)
    else:
        print(1)
    exit()
for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
maximum = max(freq.values())
for i in freq:
    if freq[i] == maximum:
        for a in range(num):
            if numbers[a] == i:
                continue
            low, high = a + 1, num
            while high - low > 1:
                mid = (low + high) // 2
                avg = (numbers[a] + numbers[mid]) / 2
                if avg == i:
                    print(maximum + 2)
                    exit()
                elif avg < i:
                    low = mid
                else:
                    high = mid
print(maximum + 1)
