import sys
input = sys.stdin.readline


numCases = int(input())
for i in range(numCases):
    whatToPrint = "Yes"
    numbers = [input()[:-1] for j in range(3)]
    for q in numbers:
        if numbers.count(q) > 1:
            whatToPrint = "No"
            break
        for num in numbers:
            if len(num) > len(q):
                if num[:len(q)] == q or num[-len(q):] == q:
                    whatToPrint = "No"
                    break
        if whatToPrint == "No":
            break
    print(whatToPrint)
