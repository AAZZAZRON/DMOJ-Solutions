x = int(input())
y = int(input())
average = x * y
remainder = average % 4
average //= 4
endings = [".00", ".25", ".50", ".75"]
print(str(average) + endings[remainder])
