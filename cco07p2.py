from collections import deque


lines = int(input())
snowflakes = set()
found = False
for _ in range(lines):
    snowflake = deque([int(x) for x in input().split()])
    for _ in range(6):
        snowflake.append(snowflake.popleft())
        if tuple(snowflake) in snowflakes or tuple(snowflake.__reversed__()) in snowflakes:
            found = True
            break
    snowflakes.add(tuple(snowflake))

if found:
    print("Twin snowflakes found.")
else:
    print("No two snowflakes are alike.")
# No two snowflakes are alike.
# Twin snowflakes found.