import sys
input = sys.stdin.readline


while True:
    number = int(input())
    if number == 0:
        break
    factors = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            factors.append(i)
    factors.append(number)
    if len(factors) % 2 == 1:
        dimensions = [factors[(len(factors) - 1) // 2], factors[(len(factors) - 1) // 2]]
    else:
        dimensions = [factors[(len(factors) // 2 - 1)], factors[len(factors) // 2]]
    prim = 2 * (dimensions[0] + dimensions[1])
    print("Minimum perimeter is {} with dimensions {} x {}".format(prim, dimensions[0], dimensions[1]))
