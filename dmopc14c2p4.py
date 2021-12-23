from sys import stdin
input = stdin.readline


num = int(input())
trees = [0]
[trees.append(trees[-1] + int(input())) for i in range(num)]
queries = int(input())
for i in range(queries):
    start, end = [int(x) for x in input().split()]
    print(trees[end + 1] - trees[start])
