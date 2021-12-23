import sys
input = sys.stdin.readline


n = int(input())
weights = [int(x) for x in input().split()]
freq = {}
for i in range(2 * n):
    if weights[i] in freq:
        freq[weights[i]].append(i + 1)
    else:
        freq[weights[i]] = [i + 1]
weights.sort()
output = []
counter = 0
for i in range(n):
    if weights[i] != weights[i + n]:
        counter += 1
    output.append([freq[weights[i]].pop(), freq[weights[i + n]].pop()])
print(counter)
[print(x[0], x[1]) for x in output]
