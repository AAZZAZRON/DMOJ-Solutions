import datetime

a, b = [int(x) for x in input().split()]
c, d = [int(x) for x in input().split()]
add = abs(c - a) + abs(d - b)
a, b, c, d, e, f = [int(x) for x in input().split(":")]
now = datetime.datetime(a, b, c, d, e, f, 0)
new = now + datetime.timedelta(seconds=add)
final = [str(new.year)]
if new.month < 10:
    final.append("0" + str(new.month))
else:
    final.append(str(new.month))
if new.day < 10:
    final.append("0" + str(new.day))
else:
    final.append(str(new.day))
if new.hour < 10:
    final.append("0" + str(new.hour))
else:
    final.append(str(new.hour))
if new.minute < 10:
    final.append("0" + str(new.minute))
else:
    final.append(str(new.minute))
if new.second < 10:
    final.append("0" + str(new.second))
else:
    final.append(str(new.second))
print(":".join(final))
