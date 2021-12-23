from sys import stdin
input = stdin.readline


cases = int(input())
for _ in range(cases):
    num = int(input())
    numbers = [int(x) for x in input().split()]
    numbers.sort(reverse=True)
    if num % 2 == 1:
        print(" ".join([str(x) for x in numbers]))
    else:
        if numbers == [numbers[0]] * num:
            print(-1)
        else:
            big = numbers[:num // 2]
            small = numbers[num // 2 :]
            answer = ""
            while big or small:
                answer += str(big.pop()) + " "
                if small:
                    answer += str(small.pop()) + " "
            print(answer[:-1])
