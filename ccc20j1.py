'''''''''
def dogTreats(small, medium, large):
    try:
        while True:
            happinessEquation = small + 2*medium + 3*large
            if happinessEquation >= 10:
                return 'Happy'
            else:
                return 'Sad'
    except ValueError:
    print('You did not enter a number. Please try again.')
    exit()


small = int(input('How many small treats did you give Barley?\n'))
medium = int(input('How many medium treats did you give Barley?\n'))
large = int(input('How many large treats did you give Barley?\n'))
print(dogTreats(small, medium, large))
'''''''''

S = int(input())
M = int(input())
L = int(input())

formula = S + M*2 + L*3

if formula >= 10:
    print('happy')
else:
    print('sad')
