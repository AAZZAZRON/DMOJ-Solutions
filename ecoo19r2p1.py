from sys import stdin
input = stdin.readline


for i in range(10):
    num = int(input())
    counter = 0
    emails = [input()[:-1].lower() for _ in range(num)]
    check = set()
    # print(emails)
    for email in emails:
        before, after = email.split("@")
        before = "".join(before.split("."))
        before = before.split("+")[0]
        new = before + "@" + after
        check.add(new)
    print(len(check))
