import sys


cases = int(sys.stdin.readline())
for i in range(cases):
    cars = []
    branch = [200000, 200000]
    numCars = int(sys.stdin.readline())
    carCount = 0
    for j in range(numCars):
        car = int(sys.stdin.readline())
        cars.append(car)
    cars.reverse()
    length = len(cars)
    j = 0
    while j < len(cars):
        k = cars[j]
        if carCount + 1 == k:
            cars.pop(j)
            carCount += 1
        else:
            cars.pop(j)
            branch.append(k)
        if branch[-1] > branch[-2]:
            break
        while True:
            if carCount + 1 == branch[-1]:
                branch.pop(-1)
                carCount += 1
            else:
                break
    if carCount == length:
        print("Y")
    else:
        print("N")
