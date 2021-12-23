from datetime import date


one = [int(x) for x in input().split("/")]
two = [int(x) for x in input().split("/")]
first = date(one[0], one[1], one[2])
second = date(two[0], two[1], two[2])
inBetween = second - first
print(inBetween.days)
