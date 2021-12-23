start, numDays = input().split()
print("Sun Mon Tue Wed Thr Fri Sat")
num = 1
start = int(start)
numDays = int(numDays)
string = "    " * (start - 1)
while num <= numDays:
    if len(string) == 27:
        print(string)
        if num >= 10:
            string = " "
        else:
            string = "  "
    else:
        if num >= 10:
            string += "  "
        else:
            string += "   "
    if num == 1:
        string = string[:-1]
    string += str(num)
    num += 1
print(string)
