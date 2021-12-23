import sys
input = sys.stdin.readline


while True:
    numbers = [int(x) for x in input().split()]
    num = numbers.pop(0)
    if num == 0:
        break
    numbers = [numbers[x] - numbers[x - 1] for x in range(1, num)]
    repeat = []
    done = False
    for i in range(0, num - 1):
        check = numbers[i]
        if check in repeat:
            yes = True
            for j in range(0, num, len(repeat)):
                if repeat != numbers[j:j + len(repeat)] and len(numbers[j:j + len(repeat)]) == len(repeat):
                    yes = False
                    break
                elif len(numbers[j:j + len(repeat)]) != len(repeat) and numbers[j:j + len(repeat)] != []:
                    if repeat[:len(numbers[j:])] != numbers[j:]:
                        yes = False
                        break
            if yes:
                print(len(repeat))
                done = True
                break
        repeat.append(check)
    if not done:
        print(num - 1)
