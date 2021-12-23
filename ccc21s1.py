pieces = int(input())
before, *height = [int(x) for x in input().split()]
lengths = [int(x) for x in input().split()]
area = 0
for q in range(pieces):
    i = height[q]
    area += lengths[q] * (before + i) / 2
    before = i
if area % 1 == 0:
    print(int(area))
else:
    print(area)
