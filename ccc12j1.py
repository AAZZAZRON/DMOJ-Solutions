speed_limit = int(input())
recorded_speed = int(input())
if recorded_speed <= speed_limit:
    print('Congratulations, you are within the speed limit!')
elif recorded_speed <= speed_limit + 20:
    print('You are speeding and your fine is $100.')
elif recorded_speed <= speed_limit + 30:
    print('You are speeding and your fine is $270.')
else:
    print('You are speeding and your fine is $500.')
