start = input()
end = input()
turns = int(input())

start_split = start.split()
start_x = int(start_split[0])
start_y = int(start_split[1])
end_split = end.split()
end_x = int(end_split[0])
end_y = int(end_split[1])

distance_x = abs(end_x - start_x)
distance_y = abs(end_y - start_y)

shortest = distance_x + distance_y

if shortest > turns:
    print('N')
elif shortest == turns:
    print('Y')
elif shortest % 2 == 0:
    if turns % 2 == 1:
        print('N')
    else:
        print('Y')
elif shortest % 2 == 1:
    if shortest == 1:
        if turns % 3 == 0:
            print('Y')
        else:
            print('N')
    else:
        if turns % 2 == 0:
            print('N')
        else:
            print('Y')
