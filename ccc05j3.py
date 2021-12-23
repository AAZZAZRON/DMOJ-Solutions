directions = [["HOME", input()]]
while True:
    x = input()
    if x == "SCHOOL":
        break
    direction = input()
    directions.append([x, direction])
directions.reverse()
while directions:
    street, direction = directions.pop(0)
    if direction == "R":
        direction = "LEFT"
    else:
        direction = "RIGHT"
    if not directions:
        print(f"Turn {direction} into your HOME.")
    else:
        print(f"Turn {direction} onto {street} street.")
