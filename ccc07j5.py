import sys
input = sys.stdin.readline


def driveThrough(distance, low, high, memo=None):
    if memo is None:
        memo = {}
    if distance == 7000:
        return 1
    elif distance == -1:
        return 0
    elif distance in memo:
        return memo[distance]
    hotels.append(distance + low - 1)
    hotels.append(distance + high + 1)
    hotels.sort()
    possible = [hotels[i] for i in range(hotels.index(distance + low - 1) + 1, hotels.index(distance + high + 1))]
    hotels.pop(hotels.index(distance + low - 1))
    hotels.pop(hotels.index(distance + high + 1))
    if not possible:
        possible = [-1]
    memo[distance] = 0
    for x in possible:
        memo[distance] += driveThrough(distance + (x - distance), low, high, memo)
    return memo[distance]


hotels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
min = int(input())
max = int(input())
numNewHotels = int(input())
[hotels.append(int(input())) for i in range(numNewHotels)]
hotels.sort()
print(driveThrough(0, min, max))
