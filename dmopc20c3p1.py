num = int(input())
check = [x for x in range(1, num + 1)]
presents = [int(x) for x in input().split()]
presents.sort()
if check == presents:
    print("YES")
else:
    print("NO")
