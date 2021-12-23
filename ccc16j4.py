start = input()
start_split = start.split(':')
start_hour = start_split[0]
start_minute = start_split[1]

no_rush_start = ['00', '01', '02', '03', '04', '10', '11', '12', '19', '20', '21', '22', '23']
no_rush_end = ['02', '03', '04', '05', '06', '12', '13', '14', '21', '22', '23', '00', '01']
rush_one = ['07', '08', '09']
rush_two = ['15', '16', '17', '18']
before_one = ['05', '06']
before_two = ['13', '14']

if start_hour in no_rush_start:
    x = no_rush_start.index(start_hour)
    print(no_rush_end[x] + ':' + start_minute)
elif start_hour in rush_one:
    time_hour = 9 - int(start_hour)
    time_minute = 60 - int(start_minute)
    if time_minute == 60:
        time_minute = 0
        time_hour += 1
    minutes = int((time_hour * 60 + time_minute) / 2)
    extra = 120 - minutes
    hour = 0
    while extra >= 60:
        extra = extra - 60
        hour += 1
    if extra == 0:
        extra = '00'
    print(str(10 + hour) + ':' + str(extra))
elif start_hour in rush_two:
    time_hour = 18 - int(start_hour)
    time_minute = 60 - int(start_minute)
    if time_minute == 60:
        time_minute = 0
        time_hour += 1
    minutes = int((time_hour * 60 + time_minute) / 2)
    extra = 120 - minutes
    hour = 0
    while extra >= 60:
        extra = extra - 60
        hour += 1
    if extra == 0:
        extra = '00'
    print(str(19 + hour) + ':' + str(extra))
elif start_hour in before_one:
    time_hour = 6 - int(start_hour)
    time_minute = 60 - int(start_minute)
    if time_minute == 60:
        time_minute = 0
        time_hour += 1
    minutes = int((time_hour * 60 + time_minute))
    extra = (120 - minutes)*2
    hour = 0
    while extra >= 60:
        extra = extra - 60
        hour += 1
    if extra == 0:
        extra = '00'
    y = 7 + hour
    if y < 10:
        y = '0' + str(y)

    else:
        y = str(y)
        extra = int(extra / 2)
    print(y + ':' + str(extra))
elif start_hour in before_two:
    time_hour = 14 - int(start_hour)
    time_minute = 60 - int(start_minute)
    if time_minute == 60:
        time_minute = 0
        time_hour += 1
    minutes = int((time_hour * 60 + time_minute))
    extra = (120 - minutes)*2
    hour = 0
    while extra >= 60:
        extra = extra - 60
        hour += 1
    if extra == 0:
        extra = '00'
    print(str(15 + hour) + ':' + str(extra))
