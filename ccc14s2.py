num = int(input())
partner_one = input()
partner_two = input()
partners = []
one_split = partner_one.split()
two_split = partner_two.split()

if num % 2 == 1:
    print('bad')
else:
    for i in range(0, num):
        x = [one_split[i], two_split[i]]
        partners.append(x)

    q = 0
    while q < num:
        if partners[q][0] == partners[q][1]:
            print('bad')
            q = num
        else:
            x = partners[i]
            x.reverse()
            if x in partners:
                pass
            else:
                print('bad')
                q = num
        q += 1

    if q != num + 1:
        print('good')
