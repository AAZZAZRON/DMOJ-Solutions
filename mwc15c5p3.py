one, two = [int(x) for x in input().split()]
essayOne = set()
essayTwo = set()
[essayOne.add(x) for x in input().split()]
[essayTwo.add(x) for x in input().split()]
print(len(essayOne) - len(essayOne.difference(essayTwo)))

