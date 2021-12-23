from sys import stdin
input = stdin.readline


numLines = int(input())
things = [input()[:-1] for i in range(numLines)]
day = 1
while day <= numLines:
    if day % 10 == 1 and day % 100 != 11:
        date = f"{day}st"
    elif day % 10 == 2 and day % 100 != 12:
        date = f"{day}nd"
    elif day % 10 == 3 and day % 100 != 13:
        date = f"{day}rd"
    else:
        date = f"{day}th"
    print(f"On the {date} day of Christmas my true love sent to me:")
    for x in range(day):
        if x == day - 1 and day != 1:
            print(f"and {day - x} {things[day - x - 1]}")
        else:
            print(f"{day - x} {things[day - x - 1]}")
    day += 1
