start = input()
num_shifts = int(input())
equation = start

for i in range(0, num_shifts):
    start = start + '0'
    equation = equation + '+' + start

answer = eval(equation)
print(answer)
