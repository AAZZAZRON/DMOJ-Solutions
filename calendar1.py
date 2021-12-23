import sys
input = sys.stdin.readline


heaven = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
earth = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
values = [0] * 60
for i in range(60):
    values[i] = heaven[i % 10] + earth[i % 12]
# print(values)

for _ in range(int(input())):
    print(values[(int(input()) % 60) - 4])
